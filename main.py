import psycopg2
import requests
import pandas as pd 
import json
from itertools import groupby
from datetime import date, datetime, timedelta, tzinfo, timezone

def create_body():
    select_query = ''' select distinct
                             it.lastname_p
                             , it.firstname_p
                             , it.middlename_p
                             , it.birthdate_p
		                     , e.shorttitle_p as title
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
                        limit 5'''

    connection = psycopg2.connect(user='tandemdb', password='FEfs$*dcn2slts',
                                  host='192.168.25.101', port='5432', database='tdmdb')
    cursor = connection.cursor()
    cursor.execute(select_query)
    select = cursor.fetchall()
    #print(select[0])
    #print(select[0][0], select[0][1], select[0][2],select[0][3])
    columns = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Образовательная программа']
    df = pd.DataFrame(select, columns=columns)
    #print(df)
    res = (df.groupby(['Фамилия','Имя','Отчество', 'Дата рождения'])
         [['Образовательная программа']]
         .apply(lambda x: tuple(x.values))
         .reset_index(name='eduprogram'))
    print(res.dtypes) 
    print(res)
    res = res.astype({'Фамилия': str, 'Имя': str, 'Отчество': str})
    print(res.dtypes) 

        
    #res.to_dict('records')
    
    
    #print('res: ', res, type(res))
    #result = res.to_dict('records')
    #jsonStr = json.dumps(result)
    #jsonStr = json.dumps(result, indent=4, sort_keys=True, default=str, encode='utf8')
    #print(jsonStr)
    
    
    

def send_request():
    session = requests.session()
    endpoint = "https://test.usla.ru/api/updateusereduprogram/"
    session.headers = {"Content-Type": "application/json; charset=utf-8","Authorization":"Bearer E1F3HDYw5qgfpDw05z5cM?Tvqy2K-CaAOKjb2o70Kz06"}
    body = ''

    session.headers.update({"Content-Length": str(len(body))})
    response = session.post(url=endpoint, data=body.encode('utf-8'), verify=True)
    print('test')
    print(response.text)
    return (response.text)


if __name__ == "__main__":
    create_body()
