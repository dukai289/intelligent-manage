# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
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
    first_name = models.CharField(max_length=30)
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


class CqFood(models.Model):
    id = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=128)
    health_light = models.IntegerField()
    thumb_image_url = models.CharField(max_length=255)
    large_image_url = models.CharField(max_length=255)
    calory = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=4, decimal_places=2)
    fat = models.DecimalField(max_digits=4, decimal_places=2)
    carbohydrate = models.DecimalField(max_digits=4, decimal_places=2)
    fiber_dietary = models.DecimalField(max_digits=4, decimal_places=2)
    first_category_id = models.PositiveIntegerField()
    two_category_id = models.PositiveIntegerField()
    three_category_id = models.PositiveIntegerField()
    percentage_protein = models.DecimalField(max_digits=10, decimal_places=6)
    percentage_fat = models.DecimalField(max_digits=10, decimal_places=6)
    percentage_carbohydrate = models.DecimalField(max_digits=10, decimal_places=6)
    in_recipe = models.IntegerField()
    delete_time = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    log_id = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cq_food'


class CqFoodData(models.Model):
    index = models.BigIntegerField()
    id_boohee = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    food_type = models.CharField(max_length=128)
    goods_id = models.CharField(max_length=128)
    thumb_image_url = models.CharField(max_length=128)
    large_image_url = models.CharField(max_length=128)
    updated_at = models.CharField(max_length=128)
    health_light = models.FloatField()
    lights_org = models.CharField(max_length=128)
    warnings = models.CharField(max_length=128)
    warning_scenes = models.CharField(max_length=128)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    info_calory = models.CharField(max_length=128)
    info_protein = models.CharField(max_length=128)
    info_fat = models.CharField(max_length=128)
    info_carbohydrate = models.CharField(max_length=128)
    fiber_dietary = models.FloatField()
    info_fiber_dietary = models.CharField(max_length=128)
    saturated_fat = models.FloatField()
    info_saturated_fat = models.CharField(max_length=128)
    ufa = models.FloatField()
    info_ufa = models.CharField(max_length=128)
    fatty_acid = models.FloatField()
    info_fatty_acid = models.CharField(max_length=128)
    mufa = models.FloatField()
    info_mufa = models.CharField(max_length=128)
    pufa = models.FloatField()
    info_pufa = models.CharField(max_length=128)
    dha = models.FloatField()
    info_dha = models.CharField(max_length=128)
    n_6_fatty_acids = models.FloatField()
    info_n_6_fatty_acids = models.CharField(max_length=128)
    n_9_fatty_acids = models.FloatField()
    info_n_9_fatty_acids = models.CharField(max_length=128)
    n3fa = models.FloatField()
    info_n3fa = models.CharField(max_length=128)
    cholesterol = models.FloatField()
    info_cholesterol = models.CharField(max_length=128)
    fructose = models.FloatField()
    info_fructose = models.CharField(max_length=128)
    folacin = models.FloatField()
    info_folacin = models.CharField(max_length=128)
    vitamin_a = models.FloatField()
    info_vitamin_a = models.CharField(max_length=128)
    vitamin_d = models.FloatField()
    info_vitamin_d = models.CharField(max_length=128)
    vitamin_e = models.FloatField()
    info_vitamin_e = models.CharField(max_length=128)
    vitamin_k = models.FloatField()
    info_vitamin_k = models.CharField(max_length=128)
    thiamine = models.FloatField()
    info_thiamine = models.CharField(max_length=128)
    lactoflavin = models.FloatField()
    info_lactoflavin = models.CharField(max_length=128)
    vitamin_b6 = models.FloatField()
    info_vitamin_b6 = models.CharField(max_length=128)
    vitamin_b12 = models.FloatField()
    info_vitamin_b12 = models.CharField(max_length=128)
    niacin = models.FloatField()
    info_niacin = models.CharField(max_length=128)
    pantothenic = models.FloatField()
    info_pantothenic = models.CharField(max_length=128)
    choline = models.FloatField()
    info_choline = models.CharField(max_length=128)
    biotin = models.FloatField()
    info_biotin = models.CharField(max_length=128)
    vitamin_c = models.FloatField()
    info_vitamin_c = models.CharField(max_length=128)
    natrium = models.FloatField()
    info_natrium = models.CharField(max_length=128)
    kalium = models.FloatField()
    info_kalium = models.CharField(max_length=128)
    calcium = models.FloatField()
    info_calcium = models.CharField(max_length=128)
    phosphor = models.FloatField()
    info_phosphor = models.CharField(max_length=128)
    magnesium = models.FloatField()
    info_magnesium = models.CharField(max_length=128)
    chlorine = models.FloatField()
    info_chlorine = models.CharField(max_length=128)
    iron = models.FloatField()
    info_iron = models.CharField(max_length=128)
    zinc = models.FloatField()
    info_zinc = models.CharField(max_length=128)
    copper = models.FloatField()
    info_copper = models.CharField(max_length=128)
    manganese = models.FloatField()
    info_manganese = models.CharField(max_length=128)
    chrome = models.FloatField()
    info_chrome = models.CharField(max_length=128)
    iodine = models.FloatField()
    info_iodine = models.CharField(max_length=128)
    selenium = models.FloatField()
    info_selenium = models.CharField(max_length=128)
    fluorine = models.FloatField()
    info_fluorine = models.CharField(max_length=128)
    hg = models.FloatField()
    info_hg = models.CharField(max_length=128)
    proanthocyanidin = models.FloatField()
    info_proanthocyanidin = models.CharField(max_length=128)
    quercetin = models.FloatField()
    info_quercetin = models.CharField(max_length=128)
    anthocyanin = models.FloatField()
    info_anthocyanin = models.CharField(max_length=128)
    soy_isoflavone = models.FloatField()
    info_soy_isoflavone = models.CharField(max_length=128)
    carotene = models.FloatField()
    info_carotene = models.CharField(max_length=128)
    lutein_zeaxanthin = models.FloatField()
    info_lutein_zeaxanthin = models.CharField(max_length=128)
    myricetin = models.FloatField()
    info_myricetin = models.CharField(max_length=128)
    luteolin = models.FloatField()
    info_luteolin = models.CharField(max_length=128)
    purine = models.FloatField()
    info_purine = models.CharField(max_length=128)
    units = models.CharField(max_length=128)
    blood_sugar = models.CharField(max_length=128)
    food_rank = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    sub_type = models.CharField(max_length=128)
    sub_type_3 = models.CharField(max_length=128)
    thumb_image_id = models.CharField(max_length=128)
    large_image_id = models.CharField(max_length=128)
    thumb_image_path = models.CharField(max_length=128)
    large_image_path = models.CharField(max_length=128)
    img_background_path = models.CharField(max_length=128)
    percentage_protein = models.FloatField()
    percentage_fat = models.FloatField()
    percentage_carbohydrate = models.FloatField()
    other_info = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
    insert_time = models.DateTimeField()
    in_program_use = models.IntegerField()
    type_1 = models.CharField(max_length=128)
    type_2 = models.CharField(max_length=128)
    type_3 = models.CharField(max_length=128)
    lights = models.CharField(max_length=128)
    gi = models.FloatField(db_column='GI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cq_food_data'


class CqFoodLights(models.Model):
    lights_name = models.CharField(max_length=64)
    remark = models.CharField(max_length=255)
    delete_time = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    log_id = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cq_food_lights'


class CqFoodLightsMark(models.Model):
    id = models.BigAutoField(primary_key=True)
    food_id = models.BigIntegerField()
    lights_id = models.PositiveIntegerField()
    delete_time = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    log_id = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cq_food_lights_mark'
        unique_together = (('food_id', 'lights_id'),)


class CqFoodType(models.Model):
    type_name = models.CharField(max_length=64)
    level = models.IntegerField()
    remark = models.CharField(max_length=255)
    delete_time = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    log_id = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cq_food_type'


class CqFoodTypeMark(models.Model):
    food_id = models.BigIntegerField()
    type_id = models.BigIntegerField()
    remark = models.CharField(max_length=255)
    delete_time = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    log_id = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'cq_food_type_mark'


class CqMpdDetail(models.Model):
    id_profile = models.IntegerField()
    id_food = models.BigIntegerField()
    name = models.CharField(max_length=256)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    type_1 = models.CharField(max_length=256)
    type_2 = models.CharField(max_length=256)
    type_3 = models.CharField(max_length=256)
    lights = models.CharField(max_length=256)
    health_light = models.IntegerField()
    type_lights = models.CharField(max_length=256)
    is_egg = models.IntegerField()
    is_milk = models.IntegerField()
    is_int = models.IntegerField()
    protein_lp = models.FloatField()
    fat_lp = models.FloatField()
    carbohydrate_lp = models.FloatField()
    calory_lp = models.FloatField()
    bound_u = models.FloatField()
    bound_l = models.FloatField()
    meals = models.CharField(max_length=256, blank=True, null=True)
    food_extract_select_type1 = models.CharField(max_length=256)
    food_extract_select_typelights = models.CharField(max_length=256)
    food_extract_drop = models.CharField(max_length=256)
    food_extract_replace_typelights = models.CharField(max_length=256)
    enerty_supply_ration = models.CharField(max_length=256)
    errors = models.CharField(max_length=256)
    quantity = models.FloatField()
    weight = models.FloatField()
    calory_fact = models.FloatField()
    calory_ladder = models.IntegerField()
    idx = models.IntegerField()
    line = models.CharField(max_length=256)
    week = models.CharField(max_length=256)
    day_from = models.IntegerField()
    day_to = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    file_rules = models.CharField(max_length=256)
    insert_time = models.DateTimeField()
    meals_n = models.CharField(max_length=256)
    veg_type = models.CharField(max_length=256)
    is_delete = models.IntegerField()
    hash_search = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cq_mpd_detail'
        verbose_name = 'Cq MPD Detail'
        verbose_name_plural = 'Cq MPD Detail'


class CqMpdDetail20231219(models.Model):
    id_profile = models.IntegerField()
    id_food = models.BigIntegerField()
    name = models.CharField(max_length=256)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    type_1 = models.CharField(max_length=256)
    type_2 = models.CharField(max_length=256)
    type_3 = models.CharField(max_length=256)
    lights = models.CharField(max_length=256)
    health_light = models.IntegerField()
    type_lights = models.CharField(max_length=256)
    is_egg = models.IntegerField()
    is_milk = models.IntegerField()
    is_int = models.IntegerField()
    protein_lp = models.FloatField()
    fat_lp = models.FloatField()
    carbohydrate_lp = models.FloatField()
    calory_lp = models.FloatField()
    bound_u = models.FloatField()
    bound_l = models.FloatField()
    meals = models.CharField(max_length=256, blank=True, null=True)
    food_extract_select_type1 = models.CharField(max_length=256)
    food_extract_select_typelights = models.CharField(max_length=256)
    food_extract_drop = models.CharField(max_length=256)
    food_extract_replace_typelights = models.CharField(max_length=256)
    enerty_supply_ration = models.CharField(max_length=256)
    errors = models.CharField(max_length=256)
    quantity = models.FloatField()
    weight = models.FloatField()
    calory_fact = models.FloatField()
    calory_ladder = models.IntegerField()
    idx = models.IntegerField()
    line = models.CharField(max_length=256)
    week = models.CharField(max_length=256)
    day_from = models.IntegerField()
    day_to = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    file_rules = models.CharField(max_length=256)
    insert_time = models.DateTimeField()
    meals_n = models.CharField(max_length=256)
    veg_type = models.CharField(max_length=256)
    is_delete = models.IntegerField()
    hash_search = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cq_mpd_detail_20231219'


class CqMpdDetailOld(models.Model):
    id_profile = models.IntegerField()
    id_food = models.BigIntegerField()
    name = models.CharField(max_length=256)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    type_1 = models.CharField(max_length=256)
    type_2 = models.CharField(max_length=256)
    type_3 = models.CharField(max_length=256)
    lights = models.CharField(max_length=256)
    health_light = models.IntegerField()
    type_lights = models.CharField(max_length=256)
    is_egg = models.IntegerField()
    is_milk = models.IntegerField()
    is_int = models.IntegerField()
    protein_lp = models.FloatField()
    fat_lp = models.FloatField()
    carbohydrate_lp = models.FloatField()
    calory_lp = models.FloatField()
    bound_u = models.FloatField()
    bound_l = models.FloatField()
    meals = models.CharField(max_length=256, blank=True, null=True)
    food_extract_select_type1 = models.CharField(max_length=256)
    food_extract_select_typelights = models.CharField(max_length=256)
    food_extract_drop = models.CharField(max_length=256)
    food_extract_replace_typelights = models.CharField(max_length=256)
    enerty_supply_ration = models.CharField(max_length=256)
    errors = models.CharField(max_length=256)
    quantity = models.FloatField()
    weight = models.FloatField()
    calory_fact = models.FloatField()
    calory_ladder = models.IntegerField()
    idx = models.IntegerField()
    line = models.CharField(max_length=256)
    week = models.CharField(max_length=256)
    day_from = models.IntegerField()
    day_to = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    file_rules = models.CharField(max_length=256)
    insert_time = models.DateTimeField()
    meals_n = models.CharField(max_length=256)
    veg_type = models.CharField(max_length=256)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cq_mpd_detail_old'


class CqMpdInfo(models.Model):
    id_profile = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    calory_ladder = models.IntegerField()
    idx = models.IntegerField()
    nutrients = models.CharField(max_length=1024)
    meals = models.CharField(max_length=1024)
    type_1 = models.CharField(max_length=1024)
    insert_time = models.DateTimeField()
    is_delete = models.IntegerField()
    file_rules = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'cq_mpd_info'
        verbose_name = 'Cq MPD Info'
        verbose_name_plural = 'Cq MPD Info'


class CqMpdInfo20231219(models.Model):
    id_profile = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    calory_ladder = models.IntegerField()
    idx = models.IntegerField()
    nutrients = models.CharField(max_length=1024)
    meals = models.CharField(max_length=1024)
    type_1 = models.CharField(max_length=1024)
    insert_time = models.DateTimeField()
    is_delete = models.IntegerField()
    file_rules = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'cq_mpd_info_20231219'


class CqMpdInfoOld(models.Model):
    id_profile = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    calory_ladder = models.IntegerField()
    idx = models.IntegerField()
    nutrients = models.CharField(max_length=1024)
    meals = models.CharField(max_length=1024)
    type_1 = models.CharField(max_length=1024)
    insert_time = models.DateTimeField()
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cq_mpd_info_old'


class CqMpdProfile(models.Model):
    file_rules = models.CharField(max_length=256)
    line = models.CharField(max_length=256)
    meals_n = models.CharField(max_length=256)
    veg_type = models.CharField(max_length=256)
    week = models.CharField(max_length=256)
    day_from = models.IntegerField()
    day_to = models.IntegerField()
    idx = models.IntegerField()
    calory_ladder = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    ls_id_food = models.CharField(max_length=256)
    ls_name_food = models.CharField(max_length=256)
    ls_id_food_zc = models.CharField(max_length=256)
    ls_name_food_zc = models.CharField(max_length=256)
    ls_weight = models.CharField(max_length=256, blank=True, null=True)
    info_quantity = models.CharField(max_length=1024)
    info_quantity_zc = models.CharField(max_length=1024)
    insert_time = models.DateTimeField()
    is_delete = models.IntegerField()
    update_time = models.DateTimeField()
    is_dup = models.IntegerField()
    hash_search = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cq_mpd_profile'
        verbose_name = 'Cq MPD Profile'
        verbose_name_plural = 'Cq MPD Profile'

class CqMpdProfile20231219(models.Model):
    file_rules = models.CharField(max_length=256)
    line = models.CharField(max_length=256)
    meals_n = models.CharField(max_length=256)
    veg_type = models.CharField(max_length=256)
    week = models.CharField(max_length=256)
    day_from = models.IntegerField()
    day_to = models.IntegerField()
    idx = models.IntegerField()
    calory_ladder = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    ls_id_food = models.CharField(max_length=256)
    ls_name_food = models.CharField(max_length=256)
    ls_id_food_zc = models.CharField(max_length=256)
    ls_name_food_zc = models.CharField(max_length=256)
    ls_weight = models.CharField(max_length=256, blank=True, null=True)
    info_quantity = models.CharField(max_length=1024)
    info_quantity_zc = models.CharField(max_length=1024)
    insert_time = models.DateTimeField()
    is_delete = models.IntegerField()
    update_time = models.DateTimeField()
    is_dup = models.IntegerField()
    hash_search = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cq_mpd_profile_20231219'


class CqMpdProfileOld(models.Model):
    file_rules = models.CharField(max_length=256)
    line = models.CharField(max_length=256)
    meals_n = models.CharField(max_length=256)
    veg_type = models.CharField(max_length=256)
    week = models.CharField(max_length=256)
    day_from = models.IntegerField()
    day_to = models.IntegerField()
    idx = models.IntegerField()
    calory_ladder = models.IntegerField()
    hash_value = models.CharField(max_length=256)
    ls_id_food = models.CharField(max_length=256)
    ls_name_food = models.CharField(max_length=256)
    ls_id_food_zc = models.CharField(max_length=256)
    ls_name_food_zc = models.CharField(max_length=256)
    ls_weight = models.CharField(max_length=256, blank=True, null=True)
    info_quantity = models.CharField(max_length=1024)
    info_quantity_zc = models.CharField(max_length=1024)
    insert_time = models.DateTimeField()
    is_delete = models.IntegerField()
    update_time = models.DateTimeField()
    is_dup = models.IntegerField()
    hash_search = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cq_mpd_profile_old'


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


class FoodData(models.Model):
    index = models.BigIntegerField()
    id_boohee = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    food_type = models.CharField(max_length=128)
    goods_id = models.CharField(max_length=128)
    thumb_image_url = models.CharField(max_length=128)
    large_image_url = models.CharField(max_length=128)
    updated_at = models.CharField(max_length=128)
    health_light = models.FloatField()
    lights_org = models.CharField(max_length=128)
    warnings = models.CharField(max_length=128)
    warning_scenes = models.CharField(max_length=128)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    info_calory = models.CharField(max_length=128)
    info_protein = models.CharField(max_length=128)
    info_fat = models.CharField(max_length=128)
    info_carbohydrate = models.CharField(max_length=128)
    fiber_dietary = models.FloatField()
    info_fiber_dietary = models.CharField(max_length=128)
    saturated_fat = models.FloatField()
    info_saturated_fat = models.CharField(max_length=128)
    ufa = models.FloatField()
    info_ufa = models.CharField(max_length=128)
    fatty_acid = models.FloatField()
    info_fatty_acid = models.CharField(max_length=128)
    mufa = models.FloatField()
    info_mufa = models.CharField(max_length=128)
    pufa = models.FloatField()
    info_pufa = models.CharField(max_length=128)
    dha = models.FloatField()
    info_dha = models.CharField(max_length=128)
    n_6_fatty_acids = models.FloatField()
    info_n_6_fatty_acids = models.CharField(max_length=128)
    n_9_fatty_acids = models.FloatField()
    info_n_9_fatty_acids = models.CharField(max_length=128)
    n3fa = models.FloatField()
    info_n3fa = models.CharField(max_length=128)
    cholesterol = models.FloatField()
    info_cholesterol = models.CharField(max_length=128)
    fructose = models.FloatField()
    info_fructose = models.CharField(max_length=128)
    folacin = models.FloatField()
    info_folacin = models.CharField(max_length=128)
    vitamin_a = models.FloatField()
    info_vitamin_a = models.CharField(max_length=128)
    vitamin_d = models.FloatField()
    info_vitamin_d = models.CharField(max_length=128)
    vitamin_e = models.FloatField()
    info_vitamin_e = models.CharField(max_length=128)
    vitamin_k = models.FloatField()
    info_vitamin_k = models.CharField(max_length=128)
    thiamine = models.FloatField()
    info_thiamine = models.CharField(max_length=128)
    lactoflavin = models.FloatField()
    info_lactoflavin = models.CharField(max_length=128)
    vitamin_b6 = models.FloatField()
    info_vitamin_b6 = models.CharField(max_length=128)
    vitamin_b12 = models.FloatField()
    info_vitamin_b12 = models.CharField(max_length=128)
    niacin = models.FloatField()
    info_niacin = models.CharField(max_length=128)
    pantothenic = models.FloatField()
    info_pantothenic = models.CharField(max_length=128)
    choline = models.FloatField()
    info_choline = models.CharField(max_length=128)
    biotin = models.FloatField()
    info_biotin = models.CharField(max_length=128)
    vitamin_c = models.FloatField()
    info_vitamin_c = models.CharField(max_length=128)
    natrium = models.FloatField()
    info_natrium = models.CharField(max_length=128)
    kalium = models.FloatField()
    info_kalium = models.CharField(max_length=128)
    calcium = models.FloatField()
    info_calcium = models.CharField(max_length=128)
    phosphor = models.FloatField()
    info_phosphor = models.CharField(max_length=128)
    magnesium = models.FloatField()
    info_magnesium = models.CharField(max_length=128)
    chlorine = models.FloatField()
    info_chlorine = models.CharField(max_length=128)
    iron = models.FloatField()
    info_iron = models.CharField(max_length=128)
    zinc = models.FloatField()
    info_zinc = models.CharField(max_length=128)
    copper = models.FloatField()
    info_copper = models.CharField(max_length=128)
    manganese = models.FloatField()
    info_manganese = models.CharField(max_length=128)
    chrome = models.FloatField()
    info_chrome = models.CharField(max_length=128)
    iodine = models.FloatField()
    info_iodine = models.CharField(max_length=128)
    selenium = models.FloatField()
    info_selenium = models.CharField(max_length=128)
    fluorine = models.FloatField()
    info_fluorine = models.CharField(max_length=128)
    hg = models.FloatField()
    info_hg = models.CharField(max_length=128)
    proanthocyanidin = models.FloatField()
    info_proanthocyanidin = models.CharField(max_length=128)
    quercetin = models.FloatField()
    info_quercetin = models.CharField(max_length=128)
    anthocyanin = models.FloatField()
    info_anthocyanin = models.CharField(max_length=128)
    soy_isoflavone = models.FloatField()
    info_soy_isoflavone = models.CharField(max_length=128)
    carotene = models.FloatField()
    info_carotene = models.CharField(max_length=128)
    lutein_zeaxanthin = models.FloatField()
    info_lutein_zeaxanthin = models.CharField(max_length=128)
    myricetin = models.FloatField()
    info_myricetin = models.CharField(max_length=128)
    luteolin = models.FloatField()
    info_luteolin = models.CharField(max_length=128)
    purine = models.FloatField()
    info_purine = models.CharField(max_length=128)
    units = models.CharField(max_length=128)
    blood_sugar = models.CharField(max_length=128)
    food_rank = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    sub_type = models.CharField(max_length=128)
    sub_type_3 = models.CharField(max_length=128)
    thumb_image_id = models.CharField(max_length=128)
    large_image_id = models.CharField(max_length=128)
    thumb_image_path = models.CharField(max_length=128)
    large_image_path = models.CharField(max_length=128)
    img_background_path = models.CharField(max_length=128)
    percentage_protein = models.FloatField()
    percentage_fat = models.FloatField()
    percentage_carbohydrate = models.FloatField()
    other_info = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
    insert_time = models.DateTimeField()
    in_program_use = models.IntegerField()
    type_1 = models.CharField(max_length=128)
    type_2 = models.CharField(max_length=128)
    type_3 = models.CharField(max_length=128)
    lights = models.CharField(max_length=128)
    gi = models.FloatField(db_column='GI')  # Field name made lowercase.
    calory_orig = models.FloatField()
    name_org = models.CharField(max_length=256, blank=True, null=True)
    alias = models.CharField(max_length=256, blank=True, null=True)
    bound_l = models.FloatField()
    bound_u = models.FloatField()
    in_replace_use = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_data'
        verbose_name = 'Food Data'
        verbose_name_plural = 'Food Data'



class FoodDetail(models.Model):
    # id = models.IntegerField(unique=True)
    index = models.BigIntegerField()
    id_boohee = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    food_type = models.CharField(max_length=128)
    goods_id = models.CharField(max_length=128)
    thumb_image_url = models.CharField(max_length=128)
    large_image_url = models.CharField(max_length=128)
    updated_at = models.CharField(max_length=128)
    health_light = models.FloatField()
    lights_org = models.CharField(max_length=128)
    warnings = models.CharField(max_length=128)
    warning_scenes = models.CharField(max_length=128)
    calory = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    info_calory = models.CharField(max_length=128)
    info_protein = models.CharField(max_length=128)
    info_fat = models.CharField(max_length=128)
    info_carbohydrate = models.CharField(max_length=128)
    fiber_dietary = models.FloatField()
    info_fiber_dietary = models.CharField(max_length=128)
    saturated_fat = models.FloatField()
    info_saturated_fat = models.CharField(max_length=128)
    ufa = models.FloatField()
    info_ufa = models.CharField(max_length=128)
    fatty_acid = models.FloatField()
    info_fatty_acid = models.CharField(max_length=128)
    mufa = models.FloatField()
    info_mufa = models.CharField(max_length=128)
    pufa = models.FloatField()
    info_pufa = models.CharField(max_length=128)
    dha = models.FloatField()
    info_dha = models.CharField(max_length=128)
    n_6_fatty_acids = models.FloatField()
    info_n_6_fatty_acids = models.CharField(max_length=128)
    n_9_fatty_acids = models.FloatField()
    info_n_9_fatty_acids = models.CharField(max_length=128)
    n3fa = models.FloatField()
    info_n3fa = models.CharField(max_length=128)
    cholesterol = models.FloatField()
    info_cholesterol = models.CharField(max_length=128)
    fructose = models.FloatField()
    info_fructose = models.CharField(max_length=128)
    folacin = models.FloatField()
    info_folacin = models.CharField(max_length=128)
    vitamin_a = models.FloatField()
    info_vitamin_a = models.CharField(max_length=128)
    vitamin_d = models.FloatField()
    info_vitamin_d = models.CharField(max_length=128)
    vitamin_e = models.FloatField()
    info_vitamin_e = models.CharField(max_length=128)
    vitamin_k = models.FloatField()
    info_vitamin_k = models.CharField(max_length=128)
    thiamine = models.FloatField()
    info_thiamine = models.CharField(max_length=128)
    lactoflavin = models.FloatField()
    info_lactoflavin = models.CharField(max_length=128)
    vitamin_b6 = models.FloatField()
    info_vitamin_b6 = models.CharField(max_length=128)
    vitamin_b12 = models.FloatField()
    info_vitamin_b12 = models.CharField(max_length=128)
    niacin = models.FloatField()
    info_niacin = models.CharField(max_length=128)
    pantothenic = models.FloatField()
    info_pantothenic = models.CharField(max_length=128)
    choline = models.FloatField()
    info_choline = models.CharField(max_length=128)
    biotin = models.FloatField()
    info_biotin = models.CharField(max_length=128)
    vitamin_c = models.FloatField()
    info_vitamin_c = models.CharField(max_length=128)
    natrium = models.FloatField()
    info_natrium = models.CharField(max_length=128)
    kalium = models.FloatField()
    info_kalium = models.CharField(max_length=128)
    calcium = models.FloatField()
    info_calcium = models.CharField(max_length=128)
    phosphor = models.FloatField()
    info_phosphor = models.CharField(max_length=128)
    magnesium = models.FloatField()
    info_magnesium = models.CharField(max_length=128)
    chlorine = models.FloatField()
    info_chlorine = models.CharField(max_length=128)
    iron = models.FloatField()
    info_iron = models.CharField(max_length=128)
    zinc = models.FloatField()
    info_zinc = models.CharField(max_length=128)
    copper = models.FloatField()
    info_copper = models.CharField(max_length=128)
    manganese = models.FloatField()
    info_manganese = models.CharField(max_length=128)
    chrome = models.FloatField()
    info_chrome = models.CharField(max_length=128)
    iodine = models.FloatField()
    info_iodine = models.CharField(max_length=128)
    selenium = models.FloatField()
    info_selenium = models.CharField(max_length=128)
    fluorine = models.FloatField()
    info_fluorine = models.CharField(max_length=128)
    hg = models.FloatField()
    info_hg = models.CharField(max_length=128)
    proanthocyanidin = models.FloatField()
    info_proanthocyanidin = models.CharField(max_length=128)
    quercetin = models.FloatField()
    info_quercetin = models.CharField(max_length=128)
    anthocyanin = models.FloatField()
    info_anthocyanin = models.CharField(max_length=128)
    soy_isoflavone = models.FloatField()
    info_soy_isoflavone = models.CharField(max_length=128)
    carotene = models.FloatField()
    info_carotene = models.CharField(max_length=128)
    lutein_zeaxanthin = models.FloatField()
    info_lutein_zeaxanthin = models.CharField(max_length=128)
    myricetin = models.FloatField()
    info_myricetin = models.CharField(max_length=128)
    luteolin = models.FloatField()
    info_luteolin = models.CharField(max_length=128)
    purine = models.FloatField()
    info_purine = models.CharField(max_length=128)
    units = models.CharField(max_length=128)
    blood_sugar = models.CharField(max_length=128)
    food_rank = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    sub_type = models.CharField(max_length=128)
    sub_type_3 = models.CharField(max_length=128)
    thumb_image_id = models.CharField(max_length=128)
    large_image_id = models.CharField(max_length=128)
    thumb_image_path = models.CharField(max_length=128)
    large_image_path = models.CharField(max_length=128)
    img_background_path = models.CharField(max_length=128)
    percentage_protein = models.FloatField()
    percentage_fat = models.FloatField()
    percentage_carbohydrate = models.FloatField()
    other_info = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
    insert_time = models.DateTimeField()
    in_program_use = models.IntegerField()
    type_1 = models.CharField(max_length=128)
    type_2 = models.CharField(max_length=128)
    type_3 = models.CharField(max_length=128)
    lights = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'food_detail'
        verbose_name = 'Food Detail'
        verbose_name_plural = 'Food Detail'


class FoodList(models.Model):
    # id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    health_light = models.FloatField()
    calory = models.FloatField()
    thumb_image_path = models.CharField(max_length=128)
    large_image_path = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'food_list'
        verbose_name = 'Food List'
        verbose_name_plural = 'Food List'
