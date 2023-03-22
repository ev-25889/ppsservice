-- список дисциплин по ид предподавателя -- по ид персоны
select eregt.*
--distinct it.lastname_p , it.firstname_p , it.middlename_p , erbt.fulltitle_p
from epp_real_edu_group_t eregt
join realedugroup2ppsentry_t rpt on rpt.edugroup_id = eregt.id
join pps_entry_base_t pebt on rpt.pps_id = pebt.id
join personrole_t pt on pt.id = rpt.pps_id
join person_t pt2 on pt.person_id  = pt2.id
join identitycard_t it on it.id = pt2.identitycard_id
join epp_reg_element_part_t erept on erept.id = eregt.activitypart_id
join epp_reg_base_t erbt on erbt.id = erept.registryelement_id




-- список образовательных программ по ид преподавателя или по ид персоны.
select --errt.*
	distinct
		e.guid_p as external_id
		, e.shorttitle_p as title
		--, ecpst.title_p  as direction
		--, ecpst.subjectcode_p as code_direction
		--, et.intvalue_p as start_year
		--, (et.intvalue_p + dt.lastcourse_p) as end_year
		, it.lastname_p
		, it.firstname_p
		, it.middlename_p
		--, erbt.fulltitle_p
		--, e.shorttitle_p
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