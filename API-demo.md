#### 一、接口名称

实时语音合成接口

#### 二、接口详情

 1、提供实时语音合成功能
 
 2、在v1版本基础上，增加返回pageNum，结束flag标志

#### 三、接口地址

 1、开发环境：ws://{ip}:{port}/tclient
 
 2、测试环境：ws://{ip}:{port}/tclient
 
 3、部署环境：ws://{ip}:{port}/tclient

#### 四、请求方式

websocket

#### 五、接口参数

| 序号 | 名称    | 类型   | 是否必须 | 示例值     | 描述           |
| ---- | ------- | ------ | -------- | ---------- | -------------- |
| 1    | spkid   | String | 是       | "0"  ，"1" | speaker id     |
| 2    | text    | String | 是       | 无         | 需合成文本内容 |
| 3    | pageNum | String | 否       | "1"        | 页码           |



#### 六、返回结果

| 序号 | 名称     | 类型   | 是否必须 | 示例值 | 描述     |
| ---- | -------- | ------ | -------- | ------ | -------- |
| 1    | code     | String | 是       | 200    | 无       |
| 2    | status   | String | 是       | 无     | 状态     |
| 3    | message  | String | 是       | 无     | 无       |
| 4    | pageNum  | String | 否       | 无     | 页码     |
| 5    | wav_data | String | 是       | 无     | 音频数据 |

#### 七、返回示例

JSON示例

```json
需合成文本：'仰天大笑出门去，我辈岂是蓬蒿人'
# PROCESSING
{
  "code": 200,
  "status": "Status.PROCESSING",
  "message": "text synthesis wave data processing",
  "pageNum": "12",
  "wav_data":[7, 15, 14, 8, 2, 8, 14, 14, 5, 2, 7, 20, 29, 28, 24, 17]
}

# FINISHED
{
  "code": 200,
  "status": "Status.FINISHED",
  "message": "text synthesis wave data finished",
  "pageNum": "12",
  "wav_data":[-3, -22, -34, -43, -37, -30, -24, -22, -15, -11, -5, 0, 5]
}
```

#### 八、结果代码

说明返回示例中存在编码形式的结果进行说明，例如：200，成功。

Status.PROCESSING  表示该文本内容还有后续未合成完返回内容

Status.FINISHED  表示该段文本内容合成全部完成

#### 九、注意事项

说明在接口使用过程中的注意事项，例如某些参数要求等。

#### 十、备注说明

说明在接口使用过程中的特殊事例，例如某个结果的原因说明等。