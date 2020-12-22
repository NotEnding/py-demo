# -- encoding : utf-8 --
'''
## 需要安装的几个包
名字      作用
ws4py     socket通信
scipy     保存音频
numpy     数据转换
'''
from ws4py.client.threadedclient import WebSocketClient
import ws4py.messaging
import time, json
import numpy as np
import argparse
from config import options, CODE_PATH
import sys
sys.path.append(CODE_PATH)
if options['wavform'] == 'alaw':
    from toolkit import alaw_init, alaw2linear
    alaw_init(options['alaw_A'])

class MiniClient(WebSocketClient):
    def __init__(self, url, protocols=None, extensions=None, heartbeat_freq=None):
        super(MiniClient, self).__init__(url, protocols, extensions, heartbeat_freq)
        self.data = []

    def received_message(self, msg):
        # 二进制数据流是音频数据点，将接收到的数据加上文件头保存下来即可。
        if isinstance(msg, ws4py.messaging.BinaryMessage):
            ## 这里我将数据保存下来，
            ## 此处可以自行加相应的操作将音频播放出来，
            ## 音频数据是int16，单声道，8kHz采样率。
            if options['wavform'] == 'alaw':
                wav = np.fromstring(msg.data, dtype=np.int8)
            elif options['wavform'] == 'linear':
                wav = np.fromstring(msg.data, dtype=np.int16)
            self.data.extend(wav.tolist())
        # 服务器状态信息，比如工作端服务状态已满，无法再服务当前客户端等。
        # 解析后是一个dict。
        elif isinstance(msg, ws4py.messaging.TextMessage):
            msg = json.loads(msg.data.decode('utf-8'))
            if type(msg) == dict:
                print(msg)
            self.data.extend(msg['wav_data'])

if __name__ == '__main__':
    # 发送需要合成的文本数据，可以多句，但需要以中文逗号作为分割符
    # 单独发一个结束标记<eos>，意味着不再发送数据，建议在发送结束后发送
    # 如果合成结束仍没有接收到需要合成的文本，服务器会自动断开连接，
    # 建议在接受完整数据后自动断开与服务器的连接
    #text = '在报告中，沈向洋以微软为例，诠释了座右铭“预见未来的最好方式就是去创造未来”；还提到：“目前各位同学会是第一代和机器人共同成长的人类，喜欢也好，不喜欢也罢，这件事情正在发生。”'
    text = '2015年，是全民创业的大热之年，大众创新，万众创业，激发了无数人心中被压抑的梦想。'
    #text='我，是摆过地摊的，那会儿是在2015年。所以当眼下，地摊概念炒火了之后，我表示非常的淡定，甚至于对一些想要入局地摊生意的朋友表示有话想说。作为一名有经验的地摊从业者，我还是有一定话语权的。除了地摊，黑作坊外卖、刷单什么的，也都略有涉及，有兴趣的都可以进一步探讨。2015年，是全民创业的大热之年，大众创新，万众创业激发了无数人心中被压抑的梦想，纷纷站出来大声说话。我所在的一家机构，正是基于这样的时代背景诞生的：创业咖啡。当时场景给人的感觉就是，在探讨项目期间，讲话自信点，感情生动些，融资也不过是分分钟的事儿。如此种种，不计其数。而当时，地摊经济，是在讨论中万不可提及的，这意味着你是个过于传统的人。一个伟大的想法就此诞生。和老板在市场上纠缠了半天，最终以我心目中理想的价格，拿下第一批棉拖货源，装于麻袋之中，背回家，待第二天开始售卖。回到租住的房子后，内心激动久久不能平静，晚上睡觉的时候，梦见自己地摊边“门庭若市”，产品被疯狂抢购。此刻，摊位边上确是门庭若市了，但此景非前几日梦中之景，想想便愈发委屈。今年以来，每个人的压力都足够大。'
    ## 命令行参数配置
    parser = argparse.ArgumentParser(description='only for demo')
    # 访问链接
    parser.add_argument('-u', '--url', default='ws://localhost:{}/tclient2', dest='url', help='url to link the server')
    parser.add_argument('-p', '--port', default=str(options['port']), dest='port', help='the port to be connnected, only activate when "{}" in url option')
    # 合成文本
    parser.add_argument('-t', '--text', default=text, dest='text', help='text to be synthesized')
    parser.add_argument('-s', '--speaker', default='0', dest='speaker', help='which speaker to use.')
    args = parser.parse_args()
    args.url = args.url.format(args.port) if '{}' in args.url else args.url

    try:
        # 尝试连接服务器
        ws = MiniClient(args.url)
        ws.connect()

        event = dict(spkid=args.speaker, text=args.text, pageNum='1')
        ws.send(json.dumps(event))
        # ws.send(json.dumps(event))
        # ws.send(json.dumps(event))
        ws.send('<eos>')

        while not ws.client_terminated:
            time.sleep(0.5)

        # 相应的数据(采样率8kHz)
        print('音频的时长: {}s'.format(len(ws.data) / options['sample_rate']))

        ## 如果需要保存音频供试听，可以通过如下代码保存
        import scipy.io.wavfile as wf

        if options['wavform'] == 'linear':
            norm_data = np.array(ws.data, dtype=np.int16)
        elif options['wavform'] == 'alaw':
            norm_data = np.array(alaw2linear(ws.data), dtype=np.int8)
        wf.write('syn_wav/demo-test.wav', rate=options['sample_rate'], data=norm_data)
    except Exception as e:
        print(e)

    finally:
        ws.close()
