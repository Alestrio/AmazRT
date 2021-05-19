/*
 * AmazRT  -  Parcel Management System
 * First semester Technical Degree project
 *   Copyright  (c) 2021 - 2022
 *  - Meryem KAYA @MeryemKy
 *  - Alexis LEBEL @Alestrio
 *  - Malo LEGRAND @HoesMaaad
 */

user_type_field = document.getElementById('register_radio')
lastname_field = document.getElementById('lastname_field')
firstname_field = document.getElementById('firstname_field')
login_field = document.getElementById('login_field')
pass_field = document.getElementById('pass_field')
conf_pass_field = document.getElementById('conf_pass_field')
city_field = document.getElementById('city_field')
activity_field = document.getElementById('activity_field')
id_pld_field = document.getElementById('id_pld_field')

lastname_field.style.display = 'none'
firstname_field.style.display = 'none'
login_field.style.display = 'none'
pass_field.style.display = 'none'
conf_pass_field.style.display = 'none'
city_field.style.display = 'none'
activity_field.style.display = 'none'
id_pld_field.style.display = 'none'


user_type_field.onclick = function () {
    lastname_field.style.display = 'inline'
    firstname_field.style.display = 'inline'
    login_field.style.display = 'inline'
    pass_field.style.display = 'inline'
    conf_pass_field.style.display = 'inline'
    if (document.getElementById('user_type_field-0').checked) { //if customer is selected
        activity_field.style.display = "none"
        city_field.style.display = "inline"
        id_pld_field.style.display = "none"
    } else if (document.getElementById('user_type_field-1').checked) { //if operator is selected
        activity_field.style.display = "none"
        city_field.style.display = "none"
        id_pld_field.style.display = "inline"
    } else {
        activity_field.style.display = "inline"
        city_field.style.display = "inline"
        id_pld_field.style.display = "none"
    }
}