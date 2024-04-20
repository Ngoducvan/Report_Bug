import requests
import json
from urllib.parse import urlparse, parse_qs
def main():
    session = requests.Session()
    url = "https://api.azota.vn/api/Auth/LoginWeb"

    payloadAdmin = {
        "phone": "lethithuhien1988do@gmail.com",
        "password": "lethithuhien1988do",
        "tokenCaptcha": "03AFcWeA5uQwXb6SG6NV2UIvfRuho7nSUOqSK3sVdBTTEkOIRIbsUeTatytHmH44R4UEpbZOcU8bCb63Gi15oUIryCiNvPZ1I1gGa4e2lO5dRl1GgdLcP7grE-CfLlmSXFlfi0tJD0eIeWvsJnNoiNa9wtP3vR64rayPJ_Ntpoh62eELIuGcpBJSIy02GkaEPzsU0jBbG6zgKHIP8XZPDI8J6G4ZY9npuKEpq_H5VXCvTWsjkC6vhktgRIPwbOP2Q_7PVGPkhUApxR754T3Ig3ovUiOzkmL-xZV78FhtmKAWHHEUAsaqmkhBQ_TPUPo8msl166mSBaeyNhpdqvTaOsV1R6-vPaBVE-A7uvBOPm0CVvB3NqtyaEwI8UOzHVO5LeZKiuj9c4IHsV43OL4-Yt2RDWI65Ey2tNZG7cRR1N_15elC3D-5JgNg0sui6uewAX-cjteKbF8xWvYPjzQEEL7UkCG1WNOQpTODEYQNmQWIAonEOJ4PvIgHfU73LZugZQ4w_qZea9eVrP62atxMEwqB86RBfQEoBgCTgCnss2wa20JYyY4tMvvc_80o_lKmrPPMJ6DWtSn0tFH8beAWh-EWKX9TBd4hjnNg",
        "domain": ""
    }

    headersAdmin = {
        "Host": "api.azota.vn",
        "Content-Length": "704",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "Accept": "application/json",
        "Content-Type": "application/json-patch+json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": "Bearer",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Origin": "https://azota.vn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://azota.vn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    headersGetAnswers ={
        "Host": "api.azota.vn",
        "Content-Length": "126",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "Accept": "application/json",
        "Content-Type": "application/json-patch+json",
        "Sec-Ch-Ua-Mobile": "?1",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjkwOTEyNDAwIiwiZnVsbF9uYW1lIjoieeG6v24gaG_DoG5nIiwiZW1haWwiOiJuZ29kdWN2YW4xMTA4MjAwNkBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImF2YXRhciI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lIS3ZDYk9wUXQybnhFQllEMkJ2MkR2V2lGUTdZZUFJNGRUVUpFQ3dnZz1zOTYtYyIsImJpcnRoZGF5IjoiIiwiYW1vdW50IjoiMCIsImdlbmRlciI6IjAiLCJ6YWxvX2lkIjoiIiwicm9sZXMiOiJ7XCIkaWRcIjpcIjFcIixcIlBBUkVOVFwiOjEsXCJTVFVERU5UXCI6MSxcIlRFQUNIRVJcIjoxfSIsInBhc3N3b3JkIjoiYWU5NzU3YTZhZTIwZDJhNmVkNjNiODY5ZGU3ZWVkNTEiLCJhbGxvd19za2lwX3ZlcmlmeSI6IjIiLCJsYXN0X2FjdGl2aXR5IjoiMjAyMy0xMi0yMSAxMDowMTo0MSIsImxhbmd1YWdlIjoidmkiLCJuYmYiOjE3MDMxMjc3MDEsImV4cCI6MTczNDIzMTcwMSwiaWF0IjoxNzAzMTI3NzAxfQ.R2hGyix-jznaJ5irz2wcXs9Qz182inbKuygRoLAXLag",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Origin": "https://azota.vn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://azota.vn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    
    loginAdmin = session.post(url, json=payloadAdmin, headers=headersAdmin)
    print("Đăng nhập Admin thành công")
    user_input_link = input("Nhập link azota: ")
    parsed_url = urlparse(user_input_link)

    query_params = parse_qs(parsed_url.query)

    question_ids_str = query_params.get('questionIds', [''])[0]

    question_ids_array = question_ids_str.split(',')
    question_number = 1
    for question_id in question_ids_array:
        payloadGetAnswer={
        "exceptQuestionIds":[],
        "matrix":[{"number":1,
         "key": f"[@Q{question_id}:Câu hỏi]=>0",
        "paths":[{"type":"QUEST",
        "id":question_id}]}]}
        urlAnswer="https://api.azota.vn/api/questions/matrix"
        getAnswer=session.post(urlAnswer, json=payloadGetAnswer,headers=headersGetAnswers)
        y = json.loads(getAnswer.text)
        content=y["data"][0]["questions"][0]["answerConfig"]
        data = json.loads(content)
        contents = []
        for item in data:
            contents.append(item["content"])
        result_value= y["data"][0]["questions"][0]["answerResult"][2]
        if result_value == "A":
            message=f"Câu {question_number}: "  + " --- " + contents[0]
            print(message)
        elif result_value == "B":
            message=f"Câu {question_number}: "  + " --- " + contents[1]
            print(message)
        elif result_value == "C":
            message=f"Câu {question_number}: "  + " --- " + contents[2]
            print(message)
        elif result_value == "D":
            message=f"Câu {question_number}: "  + " --- " + contents[3]
            print(message)
        else:
            print(f"Giá trị không hợp lệ: {result_value}")
        
        question_number += 1
if __name__ == "__main__":
    main()
