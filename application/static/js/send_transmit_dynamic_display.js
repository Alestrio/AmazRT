/*
 * AmazRT  -  Parcel Management System
 * First semester Technical Degree project
 *   Copyright  (c) 2021 - 2022
 *  - Meryem KAYA @MeryemKy
 *  - Alexis LEBEL @Alestrio
 *  - Malo LEGRAND @HoesMaaad
 */

type_radio = document.getElementById('type_radio')
pld_field = document.getElementById('id_pld_field')
plr_field  = document.getElementById('id_plr_field')
dest_plr_field = document.getElementById('dest_plr_field')
parcel_id_field = document.getElementById('parcel_id_field')
pld_to_plr_field = document.getElementById('pld_to_plr_field')


pld_field.style.display = 'none'
plr_field.style.display = 'none'
dest_plr_field.style.display = 'none'
pld_to_plr_field.style.display = 'none'


type_radio.onclick = function () {
    pld_field.style.display = 'inline'
    plr_field.style.display = 'inline'
    dest_plr_field.style.display = 'inline'
    pld_to_plr_field.style.display = 'inline'
    if (document.getElementById('type_radio-0').checked) { //if send is selected
        pld_field.style.display = 'inline'
        plr_field.style.display = 'inline'
        dest_plr_field.style.display = 'none'
        pld_to_plr_field.style.display = 'inline'
    } else if (document.getElementById('type_radio-1').checked) { //if transmit is selected
        pld_field.style.display = 'none'
        plr_field.style.display = 'inline'
        dest_plr_field.style.display = 'inline'
        pld_to_plr_field.style.display = 'none'
    } else {
        pld_field.style.display = 'none'
        plr_field.style.display = 'none'
        dest_plr_field.style.display = 'none'
        pld_to_plr_field.style.display = 'none'
    }
}