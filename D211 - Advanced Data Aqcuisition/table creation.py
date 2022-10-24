contract_drop = "DROP TABLE IF EXISTS contracts"
customer_drop = "DROP TABLE IF EXISTS customers"
job_drop = "DROP TABLE IF EXISTS jobs"
location_drop = "DROP TABLE IF EXISTS locations"
payment_drop = "DROP TABLE IF EXISTS payments"
services_drop = "DROP TABLE IF EXISTS services"
survey_drop = "DROP TABLE IF EXISTS surveys"
wa_fn_drop = "DROP TABLE IF EXISTS wa_fn"

#create tables




#payment table
create_payment = ("""CREATE TABLE IF NOT EXISTS public.payment
(
    payment_id integer NOT NULL,
    payment_type text ,
    CONSTRAINT payment_pkey PRIMARY KEY (payment_id)
);
""")

#location table
create_location = ("""CREATE TABLE public.location
(
    location_id integer NOT NULL,
    zip integer,
    city varchar(20),
    state varchar(2),
    county varchar(20),
    CONSTRAINT location_pkey PRIMARY KEY (location_id)
);
""")

#job table

create_job = ("""CREATE TABLE public.job
(
    job_id integer NOT NULL,
    job_title varchar(20),
    CONSTRAINT job_pkey PRIMARY KEY (job_id)
);
""")

#contract table

create_contract = ("""CREATE TABLE public.contract
(
    contract_id integer NOT NULL,
    duration VARCHAR(30),
    CONSTRAINT contract_pkey PRIMARY KEY (contract_id)
);
""")

#customer table

create_customer = ("""CREATE TABLE public.customer
(
    customer_id text NOT NULL,
    lat numeric,
    lng numeric,
    population integer,
    children integer,
    age integer,
    income numeric,
    marital text ,
    churn text ,
    gender text ,
    tenure numeric,
    monthly_charge numeric,
    bandwidth_gp_year numeric,
    outage_sec_week numeric,
    email integer,
    contacts integer,
    yearly_equip_faiure integer,
    techie text,
    port_modem text ,
    tablet text ,
    job_id integer,
    payment_id integer,
    contract_id integer,
    location_id integer,
    CONSTRAINT customer_pkey PRIMARY KEY (customer_id),
    CONSTRAINT customer_contract_id_fkey FOREIGN KEY (contract_id)
        REFERENCES public.contract (contract_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT customer_job_id_fkey FOREIGN KEY (job_id)
        REFERENCES public.job (job_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT customer_location_id_fkey FOREIGN KEY (location_id)
        REFERENCES public.location (location_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT customer_payment_id_fkey FOREIGN KEY (payment_id)
        REFERENCES public.payment (payment_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);
""")

#create services table
services_create = ("""CREATE TABLE IF NOT EXISTS public.serices
( 
    customer_id text NOT NULL,
    InternetService text,
    PhoneService text,
    Multiple text
    OnlineSecurity text,
    OnlineBackup text,
    DeviceProtection text,
    TechSupport text
    
    CONSTRAINT customer_id_fkey FOREIGN KEY (customer_id)
        REFERENCES public.customer (customer_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);
""")

survey_create = ("""CREATE TABLE IF NOT EXISTS public.survey
(               
    customer_id text NOT NULL,
    Timely_Response text,
    Timely_Fix text,
    Timely_Replacement text,
    Reliability text,
    Options text,
    Respectful_Response text,
    Courteous text,
    Active_Listening text,
    
    CONSTRAINT customer_id_fkey FOREIGN KEY (customer_id)
        REFERENCES public.customer (customer_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
""")

create_table_queries = [create_payment, create_location, create_job, create_contract, create_customer, services_create, survey_create]
drop_table_queries = [contract_drop, customer_drop, job_drop, location_drop, payment_drop, services_drop, survey_drop, wa_fn_drop]
