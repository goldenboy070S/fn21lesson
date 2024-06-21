select * from ishchilar
where salary > all(
	select department_id from department
	where department_name = 'HR'
);

select * from ishchilar
where salary > all(
	select department_id from department
	where department_name = 'IT'
);

select * from ishchilar
where department_id = all(
	select department_id from department
	where department_name = 'Sotuv'
);

select max(salary) from ishchilar
where salary > all(
	select department_id from department
	where department_name = 'HR' 
);

select min(salary) from ishchilar
where salary > all(
	select department_id from department
	where department_name = 'IT' 
);

select avg(salary) from ishchilar
where salary >any(
	select department_id from department
	where department_name = 'Marketing'
);

select count(*) from ishchilar
where department_id = all(
	select department_id from department
	where department_name = 'IT'
);

select * from ishchilar
where salary > any(
	select department_id from department
	where department_name = 'IT'
);





