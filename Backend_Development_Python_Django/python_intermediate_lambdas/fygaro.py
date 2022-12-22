def split_string(string):
    """Split the given string and creates a list with the elements."""
    string_list = string.split(",")
    return string_list

def join_string(string_list):
    """Joins the elements list into one string."""
    joined_string = str(string_list).replace('[', '').replace("'","").replace(']', '')
    return joined_string


def join_string(string_list):
    """Joins the elements list into one string."""
    joined_string = ''
    for string in string_list:
        joined_string += string + ' '
    return joined_string

def check_sum(elements_list, element):
    validation = False
    counter = 0
    for i in elements_list:
        for iterator in elements_list[counter+1:]:
            if i+iterator == element:
                validation = True
        counter += 1
    return validation

def check_sum_GPT(arr, num):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                return True
    return False

print("ESTE ES LO QUE QUIERE VER")
print(check_sum_GPT([10, 15, 3, 7], 17)) #True
print("ESTE ES LO QUE QUIERE VER")

if __name__ == '__main__':
    split_string("manzana,naranja,pera")
    join_string(['manzana', 'naranja', 'pera'])
    val = check_sum([2, 3, 10, 6], 7)
    print(val)


class Electronics(models.Model):

    """This is an abstract clase to be extended by the
    differente electronic devices. """

    price = models.DecimalField(max_digits=2)

    brand = models.Charfield(max_length=80, blank=False, null=False)

    name = models.Charfield(max_length=80, blank=False, null=False)

    class Meta:
        abstract = True


class MobilePhone(Electronics):

    memory = models.IntegerField(help_text="Value in GB.")
    hdd = models.IntegerField(help_text="Value in GB.")

    def __str__(self):
        return self.name, self.memory, self.hdd 

class Washer(Electronics):
    volume_capacity = models.IntegerField(help_text="Value in GB.")

    @cached_property
    def milliliter_capacity(self):
        return self.volume_capacity*1000

    def __str__(self):
        return self.name, self.volume_capacity