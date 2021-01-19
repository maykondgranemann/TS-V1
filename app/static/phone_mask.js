function mask_value(o, f) {
    setTimeout(function () {
        const v = mphone(o.value);
        if (v !== o.value) {
            o.value = v;
        }
    }, 1);
}

function mask_text(o, f) {
    setTimeout(function () {
        const v = mphone(o.innerText);
        if (v !== o.innerText) {
            o.innerText = v;
        }
    }, 1);
}

function mask_form() {
    let phone = document.getElementById('phone')
    console.log(phone.value)
    if (phone.value !== '') {
        mask_value(phone)
    }
}

function mask_list() {
    let phones = document.getElementsByClassName("phone")
    for (let phone of phones) {
        phone.innerText = mphone(phone.innerText)
    }
}

function mphone(v) {
    let r = v.replace(/\D/g, "");
    r = r.replace(/^0/, "");
    if (r.length > 10) {
        r = r.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (r.length > 5) {
        r = r.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (r.length > 2) {
        r = r.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        r = r.replace(/^(\d*)/, "($1");
    }
    return r;
}