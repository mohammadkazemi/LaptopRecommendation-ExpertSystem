import tkinter as tk
from enum import Enum
import csv
from knowledge_base import Laptop, is_studio, isclerk, isdev, ishome, isgaming, limit_price_rule_checker


def laptop_maker(id, brand, model, ram, hd_type, hd_size, screen_size, price, processor_brand, processor_model,
                 clock_speed, graphic_card_brand,
                 graphic_card_size, os, weight, comments):
    laptop = Laptop(laptop=id,
                    brand=brand,
                    model=model,
                    ram=ram,
                    hd_type=hd_type,
                    hd_size=hd_size,
                    screen_size=screen_size,
                    price=price,
                    processor_brand=processor_brand,
                    processor_model=processor_model,
                    clock_speed=clock_speed,
                    gc_brand=graphic_card_brand,
                    gc_size=graphic_card_size,
                    os=os,
                    weight=weight,
                    comments=comments)

    if clock_speed:
        laptop.clock_speed = clock_speed
    else:
        laptop.clock_speed = 0
    if graphic_card_brand:
        laptop.gc_brand = graphic_card_brand
    else:
        laptop.gc_brand = ''

    if graphic_card_size:
        laptop.gc_size = graphic_card_size
    else:
        laptop.gc_size = 0

    if weight:
        laptop.weight = weight
    else:
        laptop.weight = 0
    if comments:
        laptop.comments = comments
    else:
        laptop.comments = ''

    if os:
        laptop.os = os
    else:
        laptop.os = ''
    return laptop


def database_builder():
    # reading from database
    csvfile = open("laptops.csv", newline='')
    reader = csv.DictReader(csvfile)
    i = 1
    database = [Laptop]
    for row in reader:
        row['id'] = i
        i = i + 1
        row['comments'] = row['comments'].replace('\n', ' ')
        database.append(laptop_maker(
            id=row['id'],
            brand=row['brand'],
            model=row['model'],
            ram=row['ram'],
            hd_type=row['hd_type'],
            hd_size=row['hd_size'],
            screen_size=row['screen_size'],
            price=row['price'],
            processor_brand=row['processor_brand'],
            processor_model=row['processor_model'],
            clock_speed=row['clock_speed'],
            graphic_card_brand=row['graphic_card_brand'],
            graphic_card_size=row['graphic_card_size'],
            os=row['os'],
            weight=row['weight'],
            comments=row['comments'],
        ))
    return database


# start writing gui for program
root = tk.Tk()
root.title("laptop recommendation expert system")


class States(Enum):
    LAPTOP_TYPES_STATE = 1
    UPPER_BOUND_PRICE_STATE = 2
    OFFICE_TYPE_LAPTOP_STATE = 3
    DEV_TYPE_LAPTOP_STATE = 4
    SHOW_RESULT_LAPTOPS_STATE = 5


class AllLabels(Enum):
    LAPTOP_TYPES_LABEL = 'which type of laptop do you want?'
    UPPER_BOUND_PRICE_LABEL = 'Input Upper bound on Price '
    OFFICE_TYPE_LAPTOP_LABEL = 'what kind of office laptop do you want ?'
    DEV_TYPE_LAPTOP_LABEL = 'what kind of development laptop do you want?'
    SHOW_RESULT_LAPTOPS_LABEL = 'with your choices this laptops is available :'


office_laptops = [('clerk', 108),
                  ('development', 109),
                  ('studio', 110)]

dev_laptops = [('mobile development', 104),
               ('web and scripting', 105),
               ('game development', 106),
               ('data science', 107)]

laptop_types = [("gaming", 101),
                ("home", 102),
                ("office", 103)
                ]

user_upper_bound_value = 0
laptop_choice = 0
office_laptop_choice = 0
development_laptop_choice = 0


def find_best_laps() -> [Laptop]:
    database = database_builder()
    final_database = [Laptop]
    show_to_user = [Laptop]
    # first row is column names
    del database[0]

    if laptop_choice == 101:
        # gaming
        for lap in database:
            if isgaming(lap):
                final_database.append(lap)
    if laptop_choice == 102:
        # home
        for lap in database:
            if ishome(lap):
                final_database.append(lap)
    if laptop_choice == 103:
        # office
        if office_laptop_choice == 108:
            # clerk
            for lap in database:
                if isclerk(lap):
                    final_database.append(lap)
        elif office_laptop_choice == 109:
            # development
            for lap in database:
                if isdev(lap):
                    final_database.append(lap)

            if development_laptop_choice == 104:
                # mobile development
                pass
            elif development_laptop_choice == 105:
                # web and scripting
                pass
            elif development_laptop_choice == 106:
                #  game development
                pass
            else:
                # data science
                pass
        else:
            # office -> studio
            for lap in database:
                if is_studio(lap):
                    final_database.append(lap)

    show_to_user = limit_price_rule_checker(final_database, user_upper_bound_value)
    return show_to_user


def get_all_laptops_text(best_laps: [Laptop]):
    # this function will get list of laptops and return string of that list
    final_string = ''
    for i in range(1, len(best_laps)):
        final_string += str(best_laps[i].__str__()) + '\n'

    return final_string


def render_screen(next_state: States):
    root.destroy()
    root.__init__()
    v = tk.IntVar()
    v.set(1)  # initializing the choice, i.e. Python

    def radio_btn_builder(show_choice, v, iterable_object):
        for iter_obj, val in iterable_object:
            tk.Radiobutton(root,
                           text=iter_obj,
                           padx=20,
                           variable=v,
                           command=show_choice,
                           value=val).pack(anchor=tk.W)

    def get_upper_bound_value(value):
        global user_upper_bound_value
        user_upper_bound_value = value
        return render_screen(States.SHOW_RESULT_LAPTOPS_STATE)

    def show_choice():
        global laptop_choice
        global office_laptop_choice
        global development_laptop_choice

        print(v.get())
        if v.get() == 101:
            # 'gaming',             101
            laptop_choice = 101
            return render_screen(States.UPPER_BOUND_PRICE_STATE)
        if v.get() == 102:
            # 'home',               102
            laptop_choice = 102
            return render_screen(States.UPPER_BOUND_PRICE_STATE)
        if v.get() == 103:
            # 'office',             103
            laptop_choice = 103
            return render_screen(States.OFFICE_TYPE_LAPTOP_STATE)
        if v.get() == 104:
            # 'mobile development', 104
            development_laptop_choice = 104
            return render_screen(States.UPPER_BOUND_PRICE_STATE)
        if v.get() == 105:
            # 'web and scripting',  105
            development_laptop_choice = 105
            return render_screen(States.UPPER_BOUND_PRICE_STATE)
        if v.get() == 106:
            # 'game development',   106
            development_laptop_choice = 106
            return render_screen(States.UPPER_BOUND_PRICE_STATE)
        if v.get() == 107:
            # 'data science',       107
            development_laptop_choice = 107
            return render_screen(States.UPPER_BOUND_PRICE_STATE)
        if v.get() == 108:
            # 'clerk',              108
            office_laptop_choice = 108
            return render_screen(States.UPPER_BOUND_PRICE_STATE)
        if v.get() == 109:
            # 'development',        109
            return render_screen(States.DEV_TYPE_LAPTOP_STATE)
        if v.get() == 110:
            # 'studio',             110
            return render_screen(States.UPPER_BOUND_PRICE_STATE)

    if next_state == States.LAPTOP_TYPES_STATE:
        return (tk.Label(root, text=AllLabels.LAPTOP_TYPES_LABEL.value).pack(),
                radio_btn_builder(show_choice, v, laptop_types))

    if next_state == States.UPPER_BOUND_PRICE_STATE:
        l1: tk.Label = tk.Label(
            root, text=AllLabels.UPPER_BOUND_PRICE_LABEL.value)
        ent: tk.Entry = tk.Entry(root)
        btn: tk.Button = tk.Button(root, text='Submit', fg='red',
                                   command=lambda: get_upper_bound_value(ent.get()))

        return l1.pack(), ent.pack(), btn.pack()

    if next_state == States.OFFICE_TYPE_LAPTOP_STATE:
        return (tk.Label(root, text=AllLabels.OFFICE_TYPE_LAPTOP_LABEL.value).pack(),
                radio_btn_builder(show_choice, v, office_laptops))

    if next_state == States.DEV_TYPE_LAPTOP_STATE:
        return (tk.Label(root, text=AllLabels.DEV_TYPE_LAPTOP_LABEL.value).pack(),
                radio_btn_builder(show_choice, v, dev_laptops))

    if next_state == States.SHOW_RESULT_LAPTOPS_STATE:
        best_laps: [Laptop] = find_best_laps()
        laptop_result_text = get_all_laptops_text(best_laps)
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        lbl1 = tk.Label(root, text=AllLabels.SHOW_RESULT_LAPTOPS_LABEL.value).pack()
        # lbl2 = tk.Label(root, text=laptop_result_text).pack()
        textbox = tk.Text(root)
        textbox.pack()
        textbox.insert(tk.END, laptop_result_text)
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)
        btn = tk.Button(root,
                        text="QUIT",
                        fg="red",
                        command=quit).pack()

        return (lbl1,
                textbox,
                btn)


render_screen(States.LAPTOP_TYPES_STATE)
exit_button = tk.Button(root,
                        text="QUIT",
                        fg="red",
                        command=quit).pack()

root.mainloop()
