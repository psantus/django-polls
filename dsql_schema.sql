-- Django migrations table
CREATE TABLE django_migrations (
    id integer NOT NULL PRIMARY KEY,
    app varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);

-- Content types
CREATE TABLE django_content_type (
    id integer NOT NULL PRIMARY KEY,
    name varchar(100) NOT NULL,
    app_label varchar(100) NOT NULL,
    model varchar(100) NOT NULL,
    UNIQUE (app_label, model)
);

-- Permissions
CREATE TABLE auth_permission (
    id integer NOT NULL PRIMARY KEY,
    name varchar(255) NOT NULL,
    content_type_id integer NOT NULL REFERENCES django_content_type(id),
    codename varchar(100) NOT NULL,
    UNIQUE (content_type_id, codename)
);

-- Groups
CREATE TABLE auth_group (
    id integer NOT NULL PRIMARY KEY,
    name varchar(150) NOT NULL UNIQUE
);

CREATE TABLE auth_group_permissions (
    id integer NOT NULL PRIMARY KEY,
    group_id integer NOT NULL REFERENCES auth_group(id),
    permission_id integer NOT NULL REFERENCES auth_permission(id),
    UNIQUE (group_id, permission_id)
);

-- Users
CREATE TABLE auth_user (
    id integer NOT NULL PRIMARY KEY,
    password varchar(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username varchar(150) NOT NULL UNIQUE,
    first_name varchar(150) NOT NULL,
    last_name varchar(150) NOT NULL,
    email varchar(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);

CREATE TABLE auth_user_groups (
    id integer NOT NULL PRIMARY KEY,
    user_id integer NOT NULL REFERENCES auth_user(id),
    group_id integer NOT NULL REFERENCES auth_group(id),
    UNIQUE (user_id, group_id)
);

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL PRIMARY KEY,
    user_id integer NOT NULL REFERENCES auth_user(id),
    permission_id integer NOT NULL REFERENCES auth_permission(id),
    UNIQUE (user_id, permission_id)
);

-- Admin log
CREATE TABLE django_admin_log (
    id integer NOT NULL PRIMARY KEY,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr varchar(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer REFERENCES django_content_type(id),
    user_id integer NOT NULL REFERENCES auth_user(id)
);

-- Sessions
CREATE TABLE django_session (
    session_key varchar(40) NOT NULL PRIMARY KEY,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);

-- Polls app
CREATE TABLE polls_question (
    id integer NOT NULL PRIMARY KEY,
    question_text varchar(200) NOT NULL,
    pub_date timestamp with time zone NOT NULL
);

CREATE TABLE polls_choice (
    id integer NOT NULL PRIMARY KEY,
    question_id integer NOT NULL REFERENCES polls_question(id),
    choice_text varchar(200) NOT NULL,
    votes integer NOT NULL
);
