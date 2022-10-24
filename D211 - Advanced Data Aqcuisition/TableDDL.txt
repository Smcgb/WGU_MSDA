-- Table: public.payment

-- DROP TABLE public.payment;

CREATE TABLE IF NOT EXISTS public.payment
(
    payment_id integer NOT NULL,
    payment_type text ,
    CONSTRAINT payment_pkey PRIMARY KEY (payment_id)
);


-- Table: public.location

-- DROP TABLE public.location;

CREATE TABLE public.location
(
    location_id integer NOT NULL,
    zip integer,
    city varchar(20),
    state varchar(2),
    county varchar(20),
    CONSTRAINT location_pkey PRIMARY KEY (location_id)
);

-- Table: public.job

-- DROP TABLE public.job;

CREATE TABLE public.job
(
    job_id integer NOT NULL,
    job_title varchar(20),
    CONSTRAINT job_pkey PRIMARY KEY (job_id)
);


-- Table: public.contract

-- DROP TABLE public.contract;

CREATE TABLE public.contract
(
    contract_id integer NOT NULL,
    duration VARCHAR(30),
    CONSTRAINT contract_pkey PRIMARY KEY (contract_id)
);


-- Table: public.customer

-- DROP TABLE public.customer;

CREATE TABLE public.customer
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
