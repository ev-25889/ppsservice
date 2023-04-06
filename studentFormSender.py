import requests
import json 

def send_request(data):
    session = requests.session()
    endpoint = "http://localhost:7789/?wsdl"
    session.headers = {"Content-Type": "application/json; charset=utf-8"} 
    
    response = session.post(url=endpoint, data=data, verify=True)
    print(response.text)
    return (response.text)


if __name__ == "__main__":
    
    #body =  '{"postStudent": {"StudentUID":"JSON"}}'
    endpoint = "http://localhost:7789/"
    #print(body, type(body))
    #data = json.dumps(body)
    #print(data, type(data))
    
    data = '''{"post_students": {"FirstName":"FirstName", "LastName":"LastName", 
                            "BirthDate":"BirthDate",   
                           "PassportSeries":"PassportSeries", "PassportNumber":"PassportNumber", 
                           "PassportWhoGive":"PassportWhoGive", "PassportDateGive":"PassportDateGive", 
                           "PassportDepartmentCode":"PassportDepartmentCode", 
                           "PassportAddressString":"PassportAddressString", "MiddleName":"MiddleName",
                           "PhoneNumber":"PhoneNumber", "Email":"Email", "BirthPlace":"BirthPlace"}}'''

    struct_data = '''{
                        "post_data":
                                    {
                                       "Student":{
                                                  "FirstName":"FirstName", 
                                                  "LastName":"LastName", 
                                                  "MiddleName":"MiddleName", 
                                                  "BirthDate":"BirthDate",
                                                  "PhoneNumber":"PhoneNumber", 
                                                  "Email":"Email", 
                                                  "BirthPlace":"BirthPlace"},
                                       "StudentPassport":{ 
                                                  "PassportSeries":"PassportSeries", 
                                                  "PassportNumber":"PassportNumber", 
                                                  "PassportWhoGive":"PassportWhoGive", 
                                                  "PassportDateGive":"PassportDateGive",
                                                  "PassportDepartmentCode":"PassportDepartmentCode",
                                                  "PassportAddressString":"PassportAddressString"},
                                       "Customer":{
                                                  "FirstName":"FirstName", 
                                                  "LastName":"LastName", 
                                                  "MiddleName":"MiddleName", 
                                                  "BirthDate":"BirthDate",
                                                  "PhoneNumber":"PhoneNumber", 
                                                  "Email":"Email", 
                                                  "BirthPlace":"BirthPlace"
                                                           },
                                       "CustomerPassport":{
                                                  "PassportSeries":"PassportSeries", 
                                                  "PassportNumber":"PassportNumber", 
                                                  "PassportWhoGive":"PassportWhoGive", 
                                                  "PassportDateGive":"PassportDateGive",
                                                  "PassportDepartmentCode":"PassportDepartmentCode",
                                                  "PassportAddressString":"PassportAddressString"
                                                          },
                                       "Study":{
                                                  "Учебное подразделение":"Учебное подразделение",
                                                  "Направление подготовки":"Направление подготовки",
                                                  "Магистерская программа":"Магистерская программа",
                                                  "Форма обучения":"Форма обучения",
                                                  "Оплата обучения":"Оплата обучения",
                                                  "Способ оплаты":"Способ оплаты",
                                                  "Предыдущее образование":"Предыдущее образование",
                                                  "Балл ЕГЭ":"Балл ЕГЭ",
                                                  "Комментарий":"Комментарий"
                                              }}}'''
    r1 = requests.post('http://localhost:7789/', data=struct_data.encode('utf-8'))
    print(r1.text)
    
