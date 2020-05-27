import smtplib
from email.mime.text import MIMEText
from utils.Log import *
from config.config_global import *
from base.common_method import *

from email.header import Header #定义邮件标题
from email.mime.multipart import MIMEMultipart #用于传送附件


class SendEmail(object):

    def send_main(self, pass_list, fail_list, skip_list):
        try:
            pass_num = float(len(pass_list))
            fail_num = float(len(fail_list))
            skip_num = float(len(skip_list))
            count_num = pass_num + fail_num + skip_num
            pass_fail_count = pass_num + fail_num

            pass_result = "%.2f%%" % (pass_num / pass_fail_count * 100)
            fail_result = "%.2f%%" % (fail_num / pass_fail_count * 100)

            sub = nowTime() + '运行的接口自动化测试报告'
            contents = '此次一共运行接口个数为%s个，通过个数为%s个，失败的个数为%s个，不执行的个数为%s个，成功率为%s，失败率为%s' % (
            count_num, pass_num, fail_num, skip_num, pass_result, fail_result)

            smtpserver = 'smtp.qq.com'

            user = '1030923822@qq.com'
            password = 'eggtsypdkzzgbced'

            sender = '1030923822@qq.com'
            receives = ['fujia.liu@longbridge.sg']

            # 发送邮件主题和内容
            subject = nowTime() + 'api 接口测试报告'
            # content = '<html><h1 style="color:red">contents</h1></html>'
            content = contents
            send_file = open(excelpath, 'rb').read()
            att = MIMEText(send_file, 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment;filename="run_api.xlsx"'

            msgRoot = MIMEMultipart()
            msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
            msgRoot['Subject'] = Header(subject, 'utf-8')
            msgRoot['From'] = sender
            msgRoot['To'] = ','.join(receives)
            msgRoot.attach(att)

            smtp = smtplib.SMTP_SSL(smtpserver, 465)

            smtp.helo(smtpserver)

            smtp.ehlo(smtpserver)

            smtp.login(user, password)

            smtp.sendmail(sender, receives, msgRoot.as_string())
            smtp.quit()
            logging.info("邮件发送成功！")

        except Exception as e:

            logging.info("邮件发送失败~~")
