from qiniu import Auth, put_file, etag, urlsafe_base64_encode


class QiniuUp():
    def __init__(self,bucket_name):
        access_key = '2Cr1NjNXhoWJpZ3NRtAbJw2yPhP7f0Qa_q0DfJcq'
        secret_key = 'bJWSEUKLU1xBmMZPEnT9qUKeBp_ZutBkkH5UEW9g'
        self.q = Auth(access_key, secret_key)
        # 要上传的空间
        self.bucket_name = bucket_name

    def upqiniu(self,yun,local):
        token = self.q.upload_token(self.bucket_name, yun, 3600)
        ret, info = put_file(token, yun, local)

# QiniuUp('kindle').upqiniu('92create1\1\1 (1).jpg',"C:\\Users\Administrator\Desktop\92create1\\1\\1 (1).jpg")