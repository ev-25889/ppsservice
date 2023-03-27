import psycopg2
import requests
import pandas as pd 
import json
from config import bd
from itertools import groupby
from datetime import date, datetime, timedelta, tzinfo, timezone

def create_body():
    select_query = ''' select distinct
                             it.lastname_p
                             , it.firstname_p
                             , it.middlename_p
                             , it.birthdate_p
                                 , e.shorttitle_p as title
                             --, it.guid_p                 
                        from epp_real_edu_group_t eregt
                        join realedugroup2ppsentry_t rpt on rpt.edugroup_id = eregt.id
                        join pps_entry_base_t pebt on rpt.pps_id = pebt.id
                        join personrole_t pt on pt.id = rpt.pps_id
                        join person_t pt2 on pt.person_id  = pt2.id
                        join identitycard_t it on it.id = pt2.identitycard_id
                        join epp_rgrp_row_t errt on errt.group_id = eregt.id
                        join epp_student_wpe_part_t eswpt on eswpt.id = errt.studentwpepart_id
                        join epp_student_wpe_t eswt on eswt.id =  eswpt.studentwpe_id
                        join student_t st2 on st2.id = eswt.student_id
                        join group_t gt on gt.id = st2.group_id
                        join educationyear_t et on et.id = gt.starteducationyear_id
                        join educationorgunit_t e on gt.educationorgunit_id = e.id
                        join educationlevelshighschool_t et2 on et2.id = e.educationlevelhighschool_id
                        join edu_c_pr_subject_qual_t ecpsqt on ecpsqt.id = et2.subjectqualification_id
                        join edu_c_pr_subject_t ecpst on ecpst.id = ecpsqt.programsubject_id
                        join developperiod_t dt on dt.id = e.developperiod_id
                        order by it.lastname_p
                        '''

    connection = psycopg2.connect(user=bd['TandemBD']['user'], password=bd['TandemBD']['password'],
                                  host=bd['TandemBD']['host'], port=bd['TandemBD']['port'],
                                  database=bd['TandemBD']['database'])
    cursor = connection.cursor()
    cursor.execute(select_query)
    select = cursor.fetchall()
    columns = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Образовательная программа']
    df = pd.DataFrame(select, columns=columns)
    res = (df.groupby(['Фамилия','Имя','Отчество', 'Дата рождения'])
         [['Образовательная программа']]
         .apply(lambda x: list(x.values))
         .reset_index(name='Образовательная программа'))    
    res[['Дата рождения']] = res[['Дата рождения']].apply (pd.to_datetime)
    pd.to_datetime(res['Дата рождения'], format='%Y-%m-%d')
    res['Дата рождения'] = res['Дата рождения'].astype(str)
    d = res.to_dict('records')
    #print(type(d), d)
    for i in range(len(d)):
      #print(len(d[i]['Образовательная программа']))
      d[i]['eduprogram'] = list()
      for j in range(len(d[i]['Образовательная программа'])):
        #print(d[i]['Образовательная программа'][j][0])
        dict_j = dict()
        dict_j[str(j + 1)] = d[i]['Образовательная программа'][j][0]
        d[i]['eduprogram'].append(dict_j)
      d[i].pop('Образовательная программа')
    #print(d)
    body = json.dumps(d, ensure_ascii=False).encode('utf8')
    return body.decode()

def send_request(body):
    session = requests.session()
    endpoint = "https://test.usla.ru/api/updateuserep/" 
    session.headers = {"Content-Type": "application/json; charset=utf-8","Authorization":"Bearer E1F3HDYw5qgfpDw05z5cM?Tvqy2K-CaAOKjb2o70Kz06"}
    body = body

    session.headers.update({"Content-Length": str(len(body))})
    response = session.post(url=endpoint, data=body.encode('utf-8'), verify=True)
    print('test')
    print(response.text)
    return (response.text)

if __name__ == "__main__":
    body = create_body()
    send_request(body=body)
