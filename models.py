# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreaOfSectors(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_of_sectors'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Designation(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class KeySkills(models.Model):
    skills = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'key_skills'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Experience(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'experience'


class JobOpenings(models.Model):
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    keyskills = models.CharField(max_length=100)
    exprience = models.CharField(max_length=11)
    description = models.CharField(max_length=252)
    designation = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=50)
    e_date = models.DateField()
    p_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'job_openings'


class JobPost(models.Model):
    job_type = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    qualification = models.CharField(max_length=50, blank=True, null=True)
    job_location = models.CharField(max_length=50, blank=True, null=True)
    year_of_passing = models.CharField(max_length=50, blank=True, null=True)
    pre_cgpa = models.FloatField(blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    area_of_sector = models.CharField(max_length=50, blank=True, null=True)
    exp = models.CharField(max_length=50, blank=True, null=True)
    number_of_vacancies = models.IntegerField(blank=True, null=True)
    lasr_date_application = models.CharField(max_length=50, blank=True, null=True)
    hiring_process = models.CharField(max_length=50, blank=True, null=True)
    salary_range = models.CharField(max_length=50, blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    r_id = models.CharField(max_length=50, blank=True, null=True)
    pay_count = models.CharField(max_length=20)
    post_date = models.CharField(max_length=50, blank=True, null=True)
    application = models.CharField(max_length=50)
    technology = models.CharField(max_length=50, blank=True, null=True)
    job_desc = models.CharField(max_length=250, blank=True, null=True)
    written_test = models.CharField(max_length=10)
    group_discussion = models.CharField(max_length=10)
    technical_round = models.CharField(max_length=10)
    hr_round = models.CharField(max_length=10)
    meta_desc = models.CharField(max_length=50, blank=True, null=True)
    meta_keyword = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_post'


class JobRole(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'job_role'


class JobTypes(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'job_types'


class JpApplayJob(models.Model):
    job_id = models.CharField(max_length=50, blank=True, null=True)
    s_email = models.CharField(max_length=150, blank=True, null=True)
    r_id = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jp_applay_job'


class JpContectUs(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    mno = models.CharField(max_length=50, blank=True, null=True)
    msg = models.CharField(max_length=250, blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jp_contect_us'


class JpFavJob(models.Model):
    job_id = models.IntegerField()
    s_email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'jp_fav_job'


class JpNotification(models.Model):
    title = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jp_notification'


class JpReview(models.Model):
    rat_rating = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    seeker_email = models.TextField(blank=True, null=True)
    recruiter_email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jp_review'



class Location(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'location'


class Qualification(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'qualification'


class Recruiter(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mno = models.CharField(max_length=20, blank=True, null=True)
    ps = models.CharField(max_length=50, blank=True, null=True)
    org_type = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    des = models.CharField(max_length=250, blank=True, null=True)
    veri = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)
    plan = models.CharField(max_length=50, blank=True, null=True)
    pay = models.CharField(max_length=50, blank=True, null=True)
    pay_date = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    month = models.CharField(max_length=50, blank=True, null=True)
    show_on_reg = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)
    pay_count = models.CharField(max_length=50, blank=True, null=True)
    paypal = models.TextField(blank=True, null=True)
    counter = models.CharField(max_length=50)
    google_id = models.TextField(blank=True, null=True)
    job_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recruiter'


class Seeker(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    mno = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ps = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    current_address = models.CharField(max_length=250, blank=True, null=True)
    p_locaion = models.CharField(max_length=50, blank=True, null=True)
    job_type = models.CharField(max_length=50, blank=True, null=True)
    qua = models.CharField(max_length=50, blank=True, null=True)
    p_year = models.CharField(max_length=20, blank=True, null=True)
    cgpa = models.CharField(max_length=20, blank=True, null=True)
    aofs = models.CharField(max_length=100, blank=True, null=True)
    exp = models.CharField(max_length=50, blank=True, null=True)
    resume = models.CharField(max_length=250, blank=True, null=True)
    veri = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)
    counter = models.CharField(max_length=10)
    status = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(max_length=500, blank=True, null=True)
    google_id = models.TextField(blank=True, null=True)
    plan = models.CharField(max_length=50)
    pay = models.CharField(max_length=50)
    pay_date = models.CharField(max_length=50)
    paypal = models.TextField()
    type = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    show_on_reg = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'seeker'


class Specialization(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'specialization'


class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    c_name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=250)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'testimonials'
