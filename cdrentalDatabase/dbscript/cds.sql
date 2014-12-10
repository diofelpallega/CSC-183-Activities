
CREATE EXTENSION pgcrypto;
CREATE TABLE cds(
	cd_id serial primary key,
	cd_name text unique,
	isrented text,
	rented_by text 

);

 
 

create or replace function
   check_cd(p_cdname text)
     returns text as
$$
   declare
      cdid1 int;
   begin
      select into cdid1 cd_id from cds
         where LOWER(cd_name) = LOWER(p_cdname);
	  
      if cdid1 isnull then
         return 'true';
		 
     else
          return 'false';
      end if; 
  end;
$$
language 'plpgsql';
-- HOW TO USE :
-- SELECT check_cd('p_cdname')
  

create or replace function
   update_cd(p_cdname text, p_isrented text, p_rentedby text)
     returns text as
$$
   declare
      cdid1 int;
   begin
      select into cdid1 cd_id from cds
         where cd_name = p_cdname;
	  
      if cdid1 isnull then
         insert into cds(cd_name,isrented,rented_by) values
            (p_cdname,p_isrented,p_rentedby);
     else
          update cds
			set cd_name = p_cdname, isrented = p_isrented, rented_by = p_rentedby 
			where cd_name = p_cdname;
      end if;
	  return 'OK';
  end;
$$
language 'plpgsql';
-- HOW TO USE :
-- SELECT update_cd('p_cdname' , "isrented",'rentedby')


create or replace function
   get_cd_borrower(p_cdname text)
     returns text as
$$
   declare
      cdid1 int;
      cdborrower1 text;
   begin
      select into cdid1 cd_id from cds
         where cd_name = p_cdname;
      select into cdborrower1 rented_by from cds
         where cd_name = p_cdname;
	  
      if cdid1 isnull then
         return 'no such CD';
     else
          return cdborrower1;
      end if;
	  return 'OK';
  end;
$$
language 'plpgsql';
-- HOW TO USE :
-- SELECT get_cd_borrower('p_cdname')
 

create or replace function
   get_cd_rentedby(p_cdid int)
     returns text as
$$
   declare
      cdid1 int; 
      cdrentedby1 text; 
   begin
      select into cdid1 cd_id from cds
         where cd_id = p_cdid;
      select into cdrentedby1 rented_by from cds
         where cd_id = p_cdid; 
 
      if cdid1 isnull then
         return 'no such CD';
     else
          return cdrentedby1;
      end if;
	  return 'OK';
  end;
$$
language 'plpgsql';
-- HOW TO USE :
-- SELECT get_cd_rentedby('p_cdid')


create or replace function
   get_cd_isrented(p_cdid int)
     returns text as
$$
   declare
      cdid1 int;
      cdisrented1 text;
   begin
      select into cdid1 cd_id from cds
         where cd_id = p_cdid; 
      select into cdisrented1 isrented from cds
         where cd_id = p_cdid;
 
      if cdid1 isnull then
         return 'no such CD';
     else
          return cdisrented1;
      end if;
	  return 'OK';
  end;
$$
language 'plpgsql';
-- HOW TO USE :
-- SELECT get_cd_isrented('p_cdid')





create or replace function
   get_cd_name(p_cdid int)
     returns text as
$$
   declare
      cdid1 int;
      cdname1 text;
   begin
      select into cdid1 cd_id from cds
         where cd_id = p_cdid; 
      select into cdname1 cd_name from cds
         where cd_id = p_cdid;
 
      if cdid1 isnull then
         return 'no such CD';
     else
          return cdname1;
      end if;
	  return 'OK';
  end;
$$
language 'plpgsql';
-- HOW TO USE :
-- SELECT get_cd_name('p_cdid')





--view
create or replace function
   get_cd_perid(in int, out int,out text, out text, out text )
returns setof record as
$$
	select cd_id,cd_name, isrented, rented_by  from cds
	where cd_id = $1;

$$
  language 'sql';

-- HOW TO USE:
-- select * from get_cd_perid(cdid)

 
 


