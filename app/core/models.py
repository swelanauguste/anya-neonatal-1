from django.db import models
from django.utils import timezone

NORMAL = "N"
CRITICAL = "C"
HEALTH_STATUS_CHOICES = (
    (NORMAL, "Normal"),
    (CRITICAL, "Critical"),
)

YES = "Y"
NO = "N"
YES_NO_CHOICES = (
    (YES, "Yes"),
    (NO, "No"),
)

NORMAL = "N"
COMA = "C"
ALERTNESS_CHOICES = (
    (NORMAL, "Normal"),
    (COMA, "Coma"),
)

AIR = "A"
LAND = "L"
TRANSPORT_TYPE_CHOICES = (
    (AIR, "Air"),
    (LAND, "Land"),
)

SAME_PLACE = "S"
OTHER_PLACE = "O"
HOME = "H"
DEAD = "D"
STAYS_AT_CHOICES = (
    (SAME_PLACE, "Same place"),
    (OTHER_PLACE, "Other place"),
    (HOME, "Home"),
    (DEAD, "Dead"),
)

SAME_PLACE = "S"
RE_ADMISSION = "RA"
TRANSPORT_FROM_CHOICES = (
    (SAME_PLACE, "Same place (delivery room)"),
    (OTHER_PLACE, "Other place"),
    (RE_ADMISSION, "Re-admission"),
)

MALE = "M"
FEMALE = "F"
UNSPECIFIED = "U"
OTHER = "O"
GENDER_CHOICES = (
    (UNSPECIFIED, "Unspecified"),
    (MALE, "Male"),
    (FEMALE, "Female"),
    (OTHER, "Other"),
)

DIRECT = "D"
PHONE = "P"
NOT_DONE = "ND"
FIRST_REPORT_CHOICES = (
    (DIRECT, "Direct"),
    (PHONE, "Phone"),
    (NOT_DONE, "Not done"),
)

NOT_APPLICABLE = "N/A"
IND_OPHT_CHOICES = (
    (YES, "Yes"),
    (NO, "No"),
    (NOT_APPLICABLE, "N/A"),
)
ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
ROP_MAX_GRADE_CHOICES = (
    (ZERO, "0"),
    (ONE, "1"),
    (TWO, "2"),
    (THREE, "3"),
    (FOUR, "4"),
    (FIVE, "5"),
)
BRAIN_MAX_GRADE_CHOICES = (
    (ONE, "1"),
    (TWO, "2"),
    (THREE, "3"),
    (FOUR, "4"),
)


class SpecialCare(models.Model):
    sip = models.CharField("SIP", max_length=1, choices=YES_NO_CHOICES, default=YES)
    pob = models.CharField("place of birth", max_length=255)
    name = models.CharField(max_length=255)
    id_band = models.CharField(
        "ID band", max_length=1, choices=YES_NO_CHOICES, default=YES
    )
    neo_record_no = models.CharField(
        "neonatal record number", max_length=255, null=True
    )
    mat_record_no = models.CharField(
        "maternal record number", max_length=255, null=True
    )
    mother_name = models.CharField("mother's name", max_length=255)

    stays_at = models.CharField(
        "Stays at", max_length=1, choices=STAYS_AT_CHOICES, default=SAME_PLACE
    )
    health_status = models.CharField(
        "Health status", max_length=1, choices=HEALTH_STATUS_CHOICES, default=NORMAL
    )
    idd_new_born = models.CharField(
        "Identified her newborn", max_length=1, choices=YES_NO_CHOICES, default=YES
    )
    father_name = models.CharField(
        "father's name", max_length=255, null=True, blank=True
    )
    father_addr = models.CharField(
        "father's address", max_length=255, null=True, blank=True
    )
    father_email = models.EmailField("father's email", null=True, blank=True)
    father_phone = models.TextField("father's phones", blank=True, null=True)
    trans_from = models.CharField(
        "Transport from",
        max_length=2,
        choices=TRANSPORT_FROM_CHOICES,
        default=SAME_PLACE,
    )
    trans_reason = models.CharField(
        "reason for admission", max_length=255, null=True, blank=True
    )
    transport_type = models.CharField(
        "Transport Type", max_length=1, choices=TRANSPORT_TYPE_CHOICES, default=LAND
    )
    trans_km = models.CharField(
        "distance", max_length=4, null=True, blank=True, help_text="KM"
    )
    trans_dura = models.CharField(
        "duration",
        max_length=4,
        null=True,
        blank=True,
        help_text="HH/MM | (02/45) | 2 hrs 45 mins",
    )
    incubator = models.CharField(
        "Incubator", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    iv = models.CharField("I/V", max_length=1, choices=YES_NO_CHOICES, default=NO)
    monitors = models.CharField(
        "Monitors", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    oxygen = models.CharField(max_length=1, choices=YES_NO_CHOICES, default=NO)
    cpap = models.CharField("CPAP", max_length=1, choices=YES_NO_CHOICES, default=NO)
    ettube = models.CharField(
        "ETTube", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    is_drugged = models.CharField(
        "Drugs", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    drugs = models.TextField("drugs", null=True, blank=True)
    iv_vol = models.CharField("I/V Volume", max_length=3, null=True, blank=True)
    iv_type = models.CharField("I/V Type", max_length=255, null=True, blank=True)
    trans_comp = models.CharField(
        "complication during transport",
        max_length=1,
        choices=YES_NO_CHOICES,
        default=NO,
    )
    admin_to = models.CharField("admitted to", max_length=255, null=True)
    nurse = models.CharField(max_length=255, null=True, blank=True)
    doctor = models.CharField(max_length=255, null=True, blank=True)
    admin_date_time = models.DateTimeField("date of admission", default=timezone.now)
    admin_age = models.CharField(
        "age of patient", max_length=255, null=True, help_text="DD/HH"
    )
    gest_age = models.CharField(
        "gestational age", max_length=255, null=True, help_text="WW/DDD"
    )
    ax_temp = models.CharField("axillary temperature", max_length=255, null=True)
    sa02 = models.CharField("res_supp_ saturation", max_length=255, null=True)
    fio2 = models.CharField("Fraction of inspired res_supp_", max_length=255, null=True)
    cyano = models.CharField(
        "cyanosis", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    rds = models.CharField("RDS", max_length=1, choices=YES_NO_CHOICES, default=NO)
    pale = models.CharField(max_length=1, choices=YES_NO_CHOICES, default=NO)
    diur = models.CharField(
        "diuresis", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    alert = models.CharField(
        "alertness", max_length=1, choices=ALERTNESS_CHOICES, default=NORMAL
    )
    seizures = models.CharField(max_length=1, choices=YES_NO_CHOICES, default=NO)
    weight = models.CharField("weight (g)", max_length=4, null=True)
    length = models.CharField("length (cm)", max_length=3, null=True)
    head_c = models.CharField("head circumference (cm)", max_length=3, null=True)
    age = models.CharField(max_length=4, null=True)
    address = models.CharField(max_length=255, null=True)
    parity = models.CharField(max_length=50, null=True)
    lmp = models.CharField("LMP", max_length=50, null=True)
    edd = models.CharField("EDD", max_length=50, null=True)
    ga = models.CharField("GA", max_length=50, null=True)
    hep_b = models.CharField("Hep B", max_length=50, null=True)
    hiv = models.CharField("HIV", max_length=50, null=True)
    vdrl = models.CharField("VDRL", max_length=50, null=True)
    rub = models.CharField("Rubella", max_length=50, null=True)
    hb_elec = models.CharField("Hb elec", max_length=50, null=True)
    gp_rh = models.CharField("Gp/Rh", max_length=50, null=True)
    anc = models.CharField("ANC", max_length=50, null=True)
    dob = models.DateField("date of birth", null=True)
    tob = models.TimeField("Time of birth", null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=UNSPECIFIED)
    apgars = models.CharField(max_length=50, null=True)
    bwt = models.CharField("BWT", max_length=50, null=True)
    hc = models.CharField("HC", max_length=50, null=True)
    length1 = models.CharField(max_length=50, null=True)
    delivery_type = models.CharField("type of delivery", max_length=50, null=True)
    first_report = models.CharField(
        "1st report to family",
        choices=FIRST_REPORT_CHOICES,
        max_length=2,
        null=True,
        default=DIRECT,
    )
    diseases = models.CharField(max_length=1, choices=YES_NO_CHOICES, default=NO)
    birth_asp = models.CharField(
        "birth asphyxia", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    hmd = models.CharField("HMD", max_length=1, choices=YES_NO_CHOICES, default=NO)
    rds_meconium = models.CharField(
        "RDS w/meconium", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    pphn = models.CharField("PPHN", max_length=1, choices=YES_NO_CHOICES, default=NO)
    pda = models.CharField(
        "PDA", max_length=1, choices=YES_NO_CHOICES, default=NO, help_text="Treated?"
    )
    apneas = models.CharField(
        max_length=1, choices=YES_NO_CHOICES, default=NO, help_text="Treated?"
    )
    pneum = models.CharField(
        "pneumothorax",
        max_length=1,
        choices=YES_NO_CHOICES,
        default=NO,
    )
    bpd = models.CharField("BPD", max_length=1, choices=YES_NO_CHOICES, default=NO)
    nec = models.CharField("NEC", max_length=1, choices=YES_NO_CHOICES, default=NO)
    sbp = models.CharField(
        "Single bowel perforation", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    syp = models.CharField("syphilis", max_length=1, choices=YES_NO_CHOICES, default=NO)
    per_hiv = models.CharField(
        "perinatal HIV", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    sepsis_yes_no = models.CharField(
        "SEPSIS", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    sepsis_date_treated = models.DateField("date treated", null=True)
    sepsis_agent = models.CharField("agent", max_length=255, null=True, blank=True)
    sepsis_no_agent = models.BooleanField("no agent found", default=False)
    sepsis1_yes_no = models.CharField(
        "SEPSIS1", max_length=1, choices=YES_NO_CHOICES, default=NO
    )
    sepsis1_date_treated = models.DateField("date treated", null=True)
    sepsis1_agent = models.CharField("agent", max_length=255, null=True, blank=True)
    sepsis1_no_agent = models.BooleanField("no agent found", default=False)
    sepsis2_yes_no = models.CharField(
        "SEPSIS2", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    sepsis2_date_treated = models.DateField("date treated", null=True)
    sepsis2_agent = models.CharField("agent", max_length=255, null=True, blank=True)
    sepsis2_no_agent = models.BooleanField("no agent found", default=False)
    sepsis3_yes_no = models.CharField(
        "SEPSIS3", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    sepsis3_date_treated = models.DateField("date treated", null=True)
    sepsis3_agent = models.CharField("agent", max_length=255, null=True, blank=True)
    sepsis3_no_agent = models.BooleanField("no agent found", default=False)
    ind_opht = models.CharField(
        "indirect ophthalmoscopy", max_length=3, choices=IND_OPHT_CHOICES, default=NO
    )
    first_exam_corrected_ga = models.CharField(
        "1st exam corrected GA", max_length=3, help_text="WW/DD", null=True
    )
    rop_max_grade = models.CharField(
        "max grade", max_length=1, choices=ROP_MAX_GRADE_CHOICES, default=ZERO
    )
    surg_ind = models.CharField(
        "surgery indicated", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    us_scan = models.CharField(
        "US scan", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    leukom = models.CharField(
        "leukomalacia", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    intra_hemo = models.CharField(
        "intracranial hemorrhage", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    brain_max_grade = models.CharField(
        "max grade", max_length=1, choices=BRAIN_MAX_GRADE_CHOICES, default=ONE
    )
    birth_asph_seiz = models.CharField(
        "birth asphyxia with seizures", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    other = models.CharField("Code and name", max_length=25, null=True, blank=True)
    other1 = models.CharField("Code and name", max_length=25, null=True, blank=True)
    other2 = models.CharField("Code and name", max_length=25, null=True, blank=True)
    sev_cog_def = models.CharField(
        "Severe congenital defect", max_length=25, null=True, blank=True
    )
    surf_cnt = models.CharField(
        "Surfactant", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    surf_cnt_age_first_dose = models.CharField(
        "age first dose", max_length=4, null=True, blank=True
    )

    pda_proph_indom = models.CharField(
        "PDA prophil. indometacina", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    indo_treat = models.CharField(
        "indo/ibuprof", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    teoph_cafeine = models.CharField(
        "teoph/cafeine", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    teoph_cafeine_days = models.CharField(
        "teoph/cafeine days", max_length=4, null=True, blank=True
    )
    parent_nutn = models.CharField(
        "parenteral nutrition", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    parent_nut_days = models.CharField(
        "parenteral nutrition day", max_length=4, null=True, blank=True
    )
    pre_vent_ncpap = models.CharField(
        "pre-VENT nCPAP", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    imv_ettube = models.CharField(
        "IMV-ETTube", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    imv_ettube_days_hrs = models.CharField(
        "IMV-ETTube days/hours", max_length=5, null=True, blank=True, help_text="DDD/HH"
    )
    ncpap = models.CharField("nCPAP", max_length=2, choices=YES_NO_CHOICES, default=NO)
    ncpap_days = models.CharField("nCPAP days", max_length=4, null=True, blank=True)
    res_supp_oxygen = models.CharField(
        "oxygen", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    res_supp_oxygen_days = models.CharField(
        "oxygen days", max_length=4, null=True, blank=True
    )
    ox_over_28_days = models.BooleanField("> 28 days", default=False)
    blood_prods = models.CharField(
        "blood products", max_length=2, choices=YES_NO_CHOICES, default=NO
    )
    blood_prods_vol = models.CharField(
        "blood products Volume",
        max_length=4,
        null=True,
        blank=True,
        help_text="ml Vol. total",
    )

    def __str__(self):
        return f"{self.name}"
