__author__ = 'zk'

import argparse
from ws4py.client.threadedclient import WebSocketClient
import json
import sys
import queue
import smtplib
from email.mime.text import MIMEText


class MyClient(WebSocketClient):

    def __init__(self, args):
        super(MyClient, self).__init__(args.uri)
        self.final_hyp_queue = queue.Queue()
        self.save_adaptation_state_filename = args.save_adaptation_state
        self.send_adaptation_state_filename = args.send_adaptation_state

    def opened(self):
        print('Accessing the state port of server')

    def received_message(self, m):
        response = json.loads(m.data)
        try:
            if 'num_workers_available' in response.keys() and 'num_requests_processed' in response.keys():
                print("The server is working properly")
                print(f"response:{response}")
                print('%d workers are available,%d requests has been processed' % (
                    response['num_workers_available'], response['num_requests_processed']))
        except:
            print("The server error")
            send_mail(args, 'ASR error', 'TTS Port occupied by another program')
        self.closed("Testing finished")

    def get_full_hyp(self, timeout=60):
        return self.final_hyp_queue.get(timeout)

    def closed(self, code, reason=None):
        self.final_hyp_queue.put(code)


def send_mail(args, Subject, text):
    """
    :param args: 命令行传进来的参数
    :param Subject: 邮件主题
    :param text:邮件内容
    :return:
    """
    """ 
    mailserver = "smtp.163.com"  #邮箱服务器地址
    username_send = '18947187988@163.com'  #邮箱用户名
    password = 'jiayan150124'   #邮箱密码：需要使用授权码
    username_recv = '2234251684@qq.com'  #收件人，多个收件人用逗号隔开 
    """
    mailserver = args.mailserver
    username_send = args.username_send
    password = args.password
    username_recv = args.username_recv
    mail = MIMEText(text)
    mail['Subject'] = Subject
    mail['From'] = username_send  # 发件人
    mail['To'] = username_recv  # 收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
    smtp = smtplib.SMTP(mailserver, port=25)  # 连接邮箱服务器，smtp的端口号是25
    smtp.login(username_send, password)  # 登录邮箱
    smtp.sendmail(username_send, username_recv, mail.as_string())  # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
    smtp.quit()  # 发送完毕后退出smtp


def main():
    parser = argparse.ArgumentParser(description='Command line client for kaldigstserver')
    # parser.add_argument('-u', '--uri', default="ws://localhost:8888/client/ws/status", dest="uri", help="Server websocket URI")
    parser.add_argument('-u', '--uri', default="ws://192.168.9.26:8080/status", dest="uri", help="Server websocket URI")
    parser.add_argument('--save-adaptation-state', help="Save adaptation state to file")
    parser.add_argument('--send-adaptation-state', help="Send adaptation state from file")
    parser.add_argument('--mailserver', help="Mailserver(163:smtp.163.com)")
    parser.add_argument('--username_send', help="Sender Email")
    parser.add_argument('--password', help="Password of sender")
    parser.add_argument('--username_recv', help="Recipient Email")

    args = parser.parse_args()
    ws = MyClient(args)
    print('Testing the server...')
    try:
        ws.connect()
        result = ws.get_full_hyp()
        print(result)
    except:
        print('Unable to connect to the server, please make sure the server is turned on')
        send_mail(args, 'ASR error', 'Unable to connect to the server, please make sure the server is turned on')


if __name__ == "__main__":
    main()
