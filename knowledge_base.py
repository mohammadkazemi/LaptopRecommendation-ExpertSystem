from enum import Enum


class Laptop:
    ''' laptop object model =>
    id,brand,model,ram,hd_type,hd_size,screen_size,price,processor_brand,processor_model,clock_speed,graphic_card_brand,graphic_card_size,os,weight,comments
    exmaple =>
    35,HP,Omen W 250TX,16,ssd,256,17.6,169990,intel,i7,3.6,nvidia,8,windows,2.7,"The Best Gaming is on GeForce
    Discover desktop-class gaming on a notebook with the next-generation GeForce GTX 1050M/1060M/1070M.** Plus, get improved battery life you need to game longer, unplugged."
    '''

    def __init__(self, laptop, brand, model, ram, hd_type, hd_size, screen_size, price, processor_brand,
                 processor_model, clock_speed=None, gc_brand=None, gc_size=None, os=None, weight=None,
                 comments=None
                 ):
        self.laptop = laptop
        self.brand = brand
        self.model = model
        self.ram = ram
        self.hd_type = hd_type
        self.hd_size = hd_size
        self.screen_size = screen_size
        self.price = price
        self.processor_brand = processor_brand
        self.processor_model = processor_model
        self.clock_speed = clock_speed
        self.gc_brand = gc_brand
        self.gc_size = gc_size
        self.os = os
        self.weight = weight
        self.comments = comments

    def __cmp__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __str__(self):
        return f'\n# laptop number: {self.laptop} ' \
               f'\n# brand: {self.brand} ' \
               f'\n# model: {self.model} ' \
               f'\n# ram: {self.ram} -' \
               f'\n# hd_type: {self.hd_type} -' \
               f'\n# hd_size: {self.hd_size} -' \
               f'\n# screen_size: {self.screen_size} ' \
               f'\n# price: {self.price} ' \
               f'\n# processor_brand: {self.processor_brand} ' \
               f'\n# processor_model: {self.processor_model} ' \
               f'\n# clock_speed: {self.clock_speed} ' \
               f'\n# gc_brand: {self.gc_brand}' \
               f'\n# gc_size: {self.gc_size} ' \
               f'\n# os: {self.os} ' \
               f'\n# weight: {self.weight} ' \
               f'\n# comments: {self.comments}'


laptop_choice = 0
office_laptop_choice = 0
development_laptop_choice = 0


def mohammad_sort(lap_list: [Laptop], laptop_choice, office_laptop_choice, development_laptop_choice) -> [Laptop]:
    if len(lap_list) > 1:
        best_lap: Laptop = lap_list[1]
        # gaming
        if laptop_choice == 101:
            for i in range(1, len(lap_list)):
                if float(lap_list[i].gc_size) >= float(best_lap.gc_size):
                    best_lap = lap_list[i]
        # home
        if laptop_choice == 102:
            for i in range(1, len(lap_list)):
                if float(best_lap.clock_speed) <= float(lap_list[i].clock_speed):
                    best_lap = lap_list[i]
        if laptop_choice == 103:
            # clerk
            if office_laptop_choice == 108:
                for i in range(1, len(lap_list)):
                    if float(best_lap.clock_speed) <= float(lap_list[i].clock_speed):
                        best_lap = lap_list[i]

            if office_laptop_choice == 109:
                #  mobile dev
                if development_laptop_choice == 104:
                    for i in range(1, len(lap_list)):
                        if float(best_lap.clock_speed) <= float(lap_list[i].clock_speed):
                            best_lap = lap_list[i]

                # game dev
                if development_laptop_choice == 106:
                    for i in range(1, len(lap_list)):
                        if float(best_lap.gc_size) <= float(lap_list[i].gc_size):
                            best_lap = lap_list[i]

                # web and scripting
                if development_laptop_choice == 105:
                    for i in range(1, len(lap_list)):
                        if float(best_lap.clock_speed) <= float(lap_list[i].clock_speed):
                            best_lap = lap_list[i]

                # data science
                if development_laptop_choice == 107:
                    for i in range(1, len(lap_list)):
                        if float(best_lap.gc_size) <= float(lap_list[i].gc_size):
                            best_lap = lap_list[i]

            if office_laptop_choice == 110:
                # studio
                if development_laptop_choice == 103:
                    for i in range(1, len(lap_list)):
                        if float(best_lap.clock_speed) <= float(lap_list[i].clock_speed):
                            best_lap = lap_list[i]

        return [best_lap]
    else:
        return []


class IntelModels(Enum):
    i3 = 'i3'
    i5 = 'i5'
    i7 = 'i7'
    i9 = 'i9'


# def rule_compare_storage_type(laptop_a:Laptop, laptop_b:Laptop):
#     '''ssd is better than hdd'''
#     pass


# def compare_gc_size(P, Q):
#     '''more memory is better than less memory'''
#     gc_size(P, R),
#     gc_size(Q, S),
#     X = R, Y = S,
#     X >= Y.


# def compare_weight(P, Q):
#     '''less laptop weight is better than more laptop weight'''
#     weight(P, R),
#     weight(Q, S),
#     X = R, Y = S,
#     X >= Y.


# def compare_price(P, Q):
#     '''less laptop price is better tham more laptop price'''
#     price(P, R),
#     price(Q, S),
#     X = R, Y = S,
#     X >= Y.


# def compare_screen_size(P, Q):
#     '''more laptop screen is better than less laptop screen'''
#     screen_size(P, R),
#     screen_size(Q, S),
#     X = R, Y = S,
#     X >= Y.


# def compare_processors_brand(P, Q):
#     ''' intel is better than amd '''
#     A = 1, B = 2, B > A,
#     processor_brand(P, R),
#     processor_brand(Q, S),
#     X = R, Y = S,
#     ((X = 'amd', Y = 'amd')
#      (X='intel', Y='amd')
#      (X='intel', Y='intel')).


# def compare_graphics(P, Q):
#     ''' nvidia is better than amd'''
#     ''' nvidia is better than intel'''
#     ''' amd is better than intel'''
#     A = 1, B = 2, B > A,
#     gc_brand(P, R),
#     gc_brand(Q, S),
#     X = R, Y = S,
#     ((X = 'nvidia', Y = 'amd')
#      (X='nvidia', Y='intel')
#      (X='intel', Y='intel')
#      (X='nvidia', Y='nvidia')
#      (X='amd', Y='amd')
#      (X='amd', Y='intel')).


# def compare_processors(P, Q):
#     ''' i9 is better than all '''
#     ''' i7 is better than i5, i3'''
#     ''' i5 is better than i3'''
#     A = 1, B = 2, B > A,
#     processor_model(P, R),
#     processor_model(Q, S),
#     X = R, Y = S,
#     ((X = 'i5', Y = 'i3')
#      (X='i7', Y='i3')
#      (X='i5', Y='i5')
#      (X='i3', Y='i3')
#      (X='i7', Y='i7')
#      (X='i7', Y='i5'))


# def compare_laptop(X, Y):
#     compare_price(X, Y)
#     compare_processors_brand(X, Y) # its not necessory
#     compare_processors(X, Y)
#     compare_gc_size(X, Y)
#     compare_screen_size(X, Y)


def limit_price_rule_checker(laptops: [Laptop], upper_bound):
    tmp = [Laptop]
    for lap in laptops:
        if 'price' in dir(lap):
            if int(lap.price) < int(upper_bound):
                tmp.append(lap)
    return tmp
    # return tmp
    # return list(map(lambda x: int(x.price) < int(upper_bound), laptops))


def screen_size_rule_checker(laptop: Laptop, needed_screen_size, gt: bool, lt: bool):
    if gt:
        if float(laptop.screen_size) >= needed_screen_size:
            return True
        else:
            return False
    elif lt:
        if float(laptop.screen_size) <= needed_screen_size:
            return True
        else:
            return False


def processor_brand_rule_checker(laptop: Laptop, needed_model: [IntelModels] = None):
    if str(laptop.processor_brand).lower() == "intel":
        if str(laptop.processor_model).lower() in needed_model:
            return True
        else:
            return False
    elif str(laptop.processor_brand).lower() == "amd":
        return True
    else:
        return False


def gc_size_rule_checker(laptop: Laptop, needed_memory_size, gt: bool, lt: bool):
    if gt:
        if int(laptop.gc_size) >= needed_memory_size:
            return True
        else:
            return False
    elif lt:
        if int(laptop.gc_size) <= needed_memory_size:
            return True
        else:
            return False


def os_rule_checker(laptop: Laptop, os: [str]):
    if laptop.os in os:
        return True
    return False


def ram_rule_checker(laptop: Laptop, needed_ram, gt: bool, lt: bool):
    if gt:
        if int(laptop.ram) >= needed_ram:
            return True
        else:
            return False
    elif lt:
        if int(laptop.ram) <= needed_ram:
            return True
        else:
            return False


def rule_hd_size(laptop: Laptop, needed_storage_size, gt: bool, lt: bool):
    if gt:
        if int(laptop.hd_size) >= needed_storage_size:
            return True
        else:
            return False
    elif lt:
        if int(laptop.hd_size) <= needed_storage_size:
            return True
        else:
            return False


def rule_clock_speed(laptop: Laptop, needed_clock_speed, gt: bool, lt: bool):
    if gt:
        if float(laptop.clock_speed) >= needed_clock_speed:
            return True
        else:
            return False
    elif lt:
        if float(laptop.clock_speed) <= needed_clock_speed:
            return True
        else:
            return False


def isgaming(laptop: Laptop):
    tmp = (
            ram_rule_checker(laptop=laptop, needed_ram=8, gt=True, lt=False) and
            rule_hd_size(laptop=laptop, needed_storage_size=256, gt=True, lt=False) and
            screen_size_rule_checker(laptop=laptop, needed_screen_size=15, gt=True, lt=False) and
            gc_size_rule_checker(laptop=laptop, needed_memory_size=2, gt=True, lt=False) and
            os_rule_checker(laptop=laptop, os='windows') and
            processor_brand_rule_checker(laptop=laptop, needed_model=[
                IntelModels.i5, IntelModels.i7, IntelModels.i9])
    )
    return tmp


def isdev(laptop: Laptop):
    return (ram_rule_checker(laptop=laptop, needed_ram=8, gt=True, lt=False) and
            rule_hd_size(laptop=laptop, needed_storage_size=256, gt=True, lt=False) and
            screen_size_rule_checker(laptop=laptop, needed_screen_size=14, gt=True, lt=False) and
            rule_clock_speed(laptop=laptop, needed_clock_speed=2.3, gt=True, lt=False) and
            gc_size_rule_checker(laptop=laptop, needed_memory_size=1, gt=True, lt=False) and
            os_rule_checker(laptop, ['windows', 'linux', 'mac']) and
            processor_brand_rule_checker(laptop=laptop, needed_model=[IntelModels.i5, IntelModels.i7, IntelModels.i9]))


def isclerk(laptop: Laptop):
    return (ram_rule_checker(laptop=laptop, needed_ram=2, gt=True, lt=False) and
            rule_hd_size(laptop, needed_storage_size=128, gt=True, lt=False) and
            screen_size_rule_checker(laptop, needed_screen_size=12, gt=True, lt=False) and
            processor_brand_rule_checker(laptop, needed_model=[IntelModels.i3, IntelModels.i5, IntelModels.i7,
                                                               IntelModels.i9]) and
            os_rule_checker(laptop, 'windows'))


def ishome(laptop: Laptop):
    return (ram_rule_checker(laptop=laptop, needed_ram=2, gt=True, lt=False) and
            rule_hd_size(laptop, needed_storage_size=128, gt=True, lt=False) and
            screen_size_rule_checker(laptop, needed_screen_size=13, gt=True, lt=False) and
            os_rule_checker(laptop, ['windows', 'mac'])
            )


def is_studio(laptop: Laptop):
    return (ram_rule_checker(laptop=laptop, needed_ram=16, gt=True, lt=False) and
            rule_hd_size(laptop, needed_storage_size=2014, gt=True, lt=False) and
            screen_size_rule_checker(laptop, needed_screen_size=13, gt=True, lt=False) and
            os_rule_checker(laptop, ['windows', 'mac'])
            )
