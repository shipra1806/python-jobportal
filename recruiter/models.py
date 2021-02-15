# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class AreaOfSectors(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name;
    class Meta:
        managed = False
        db_table = 'area_of_sectors'


class Designation(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name;
    class Meta:
        managed = False
        db_table = 'designation'


class Experience(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.name+"( "+self.status+ " )"
    class Meta:
        managed = False
        db_table = 'experience'

class JobTypes(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'job_types'



class Location(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'location'


class KeySkills(models.Model):
    skills = models.CharField(max_length=50)
    def __str__(self):
        return self.skills;
    class Meta:
        managed = False
        db_table = 'key_skills'

class Qualification(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'qualification'

class Specialization(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'specialization'

class Recruiter(models.Model):
        name = models.CharField(max_length=50, blank=True, null=True)
        email = models.CharField(max_length=100, blank=True, null=True)
        mno = models.CharField(max_length=20, blank=True, null=True)
        password = models.CharField(max_length=50, blank=True, null=True)
        org_type = models.CharField(max_length=50, blank=True, null=True)
        location = models.ForeignKey(Location, on_delete=models.CASCADE)
        address = models.CharField(max_length=200, blank=True, null=True)
        website = models.CharField(max_length=100, blank=True, null=True)
        des = models.CharField(max_length=250, blank=True, null=True)
        img = models.CharField(max_length=250, blank=True, null=True)
        status = models.CharField(max_length=20)

        class Meta:
            managed = False
            db_table = 'recruiter'


class JobOpenings(models.Model):
    job_type = models.ForeignKey(JobTypes,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    keyskills = models.ForeignKey(KeySkills,on_delete=models.CASCADE)
    exprience = models.ForeignKey(Experience,on_delete=models.CASCADE)
    area_of_sector=models.ForeignKey(AreaOfSectors,on_delete=models.CASCADE)
    description = models.CharField(max_length=252)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    salary_range = models.CharField(max_length=50)
    e_date = models.DateField()
    p_date = models.DateField()
    r=models.IntegerField()
    class Meta:
        managed = False
        db_table = 'job_openings'



class JobRole(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'job_role'


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




class Seeker(models.Model):
    gender = (
        ('Male', ("Male")),
        ('Female', ("Female")),
        ('Other', ("Other"))
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50)
    mno = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10,choices=gender,default='Male')
    current_address = models.CharField(max_length=250, blank=True, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobTypes,on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification,on_delete=models.CASCADE)
    p_year = models.CharField(max_length=20, blank=True, null=True)
    cgpa = models.CharField(max_length=20, blank=True, null=True)
    area_of_sector = models.ForeignKey(AreaOfSectors,on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience,on_delete=models.CASCADE)
    resume = models.FileField()
    img = models.ImageField()
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'seeker'



class Testimonials(models.Model):
    status = (
        ('approved', ("Approved")),
        ('pending', ("Pending")),
        ('deleted', ("Deleted"))
    )
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    c_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='testimonials')
    status = models.CharField(max_length=10,choices=status,default='pending')

    class Meta:
        managed = False
        db_table = 'testimonials'
