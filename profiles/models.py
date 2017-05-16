from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# This module contains the validation and set up of a Phone Number Field ( of the format +254712345678)
# from phonenumber_field.modelfields import PhoneNumberField


# Creating a new model manager, to allow for serialization of the Customer model.
class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name, email, mobile_number, national_id):
        return self.get(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        mobile_number=mobile_number,
                        national_id=national_id)


class Customer(models.Model):
    objects = PersonManager()
    first_name = models.CharField(max_length=30,)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile_number = models.PositiveIntegerField(unique=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(9999999999999999)])
    national_id = models.PositiveIntegerField(unique=True,
                                              validators=[MinValueValidator(0),
                                                          MaxValueValidator(999999999)])
    # residence = models.CharField(max_length=20)
    # occupation = models.CharField(max_length=20, blank=False)
    fully_clreared = models.BooleanField(default=False)
    date_cleared = models.DateField(auto_now_add=True)
    batch_numbers = models.IntegerField()
    mpesa_trans_id = models.CharField(max_length=30)

    def natural_key(self):
        return (self.first_name, self.last_name, self.email, self.idNumber)

    def __str__(self):
        # return ("Details for {} {}".format(self.first_name, self.last_name))
        return ("{} {}".format(self.first_name, self.last_name))

    class Meta:
        db_table = 'tbl_profiles'
        managed = True

# This model shall be associated with a Debt Model, i.e each customer has a debt/loan statement.
# profiles models.py