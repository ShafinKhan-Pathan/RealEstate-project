from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.

class Asset(models.Model):


    state_choices = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))




    amenities_choices = (

        ('Balcony', 'Balcony'),
        ('Sun Room', 'Sun Room'),
        ('Outdoor Kitchen', 'Outdoor Kitchen'),
        ('Parking', 'Parking'),
        ('Air Condition', 'Air Condition'),
        ('Alarm System', 'Alarm System'),
        ('Tennis Court', 'Tennis Court'),
        ('VolleyBall Court', 'VolleyBall Court'),
        ('Home Theatre', 'Home Theatre'),
        ('Garden', 'Garden'),
        ('Children Play Area', 'Children Play Area'),
        ('Fitness CLub', 'Fitness CLub'),
    )
    condition_choice = (
        ('Need Renovation','Need Renovation'),
        ('Average','Average'),
        ('Good','Good'),
        ('Well Maintained','Well Maintained'),
        ('Very Good','Very Good'),
        ('Excellent','Excellent'),
        ('Outstanding','Outstanding'),

    )
    owner_choice=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    def __str__(self):
        return self.asset_title

    asset_title = models.CharField(max_length=200)
    asset_id = models.CharField(max_length=200)
    state = models.CharField(choices=state_choices,max_length=100)
    city = models.CharField(max_length=200)
    price = models.IntegerField()
    area = models.CharField(max_length=200)
    bed = models.IntegerField()
    bath = models.IntegerField()
    garage = models.IntegerField()
    door = models.CharField(choices=door_choices,max_length=10)
    year = models.IntegerField(('year'),choices = year_choice)
    amenities = MultiSelectField(choices=amenities_choices, max_length=500)
    type = models.CharField(max_length=100)
    condition = models.CharField(choices=condition_choice, max_length=50)
    description = RichTextField()
    asset_photo = models.ImageField(upload_to='photos/%Y/%m/%y/')
    asset_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%y/',blank=True)
    asset_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%y/',blank=True)
    asset_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%y/',blank=True)
    asset_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%y/',blank=True)
    no_of_owner = models.CharField(choices=owner_choice,max_length=20)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
