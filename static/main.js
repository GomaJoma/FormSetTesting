"use strict";
function ucFirst(str) {
  if (!str) return str;

  return str[0].toUpperCase() + str.slice(1);
}

let form_counter = 1;
let employer_form_counter = 1;
let file_form_counter = 1;
function append_item(formset) {
    let parameters = [];
    if (formset === 'employer'){
        employer_form_counter++;
        parameters = ['lastname', 'name', 'surname', 'position', 'punishment'];
        form_counter = employer_form_counter;
    }
    else if (formset === 'file') {
        file_form_counter++;
        parameters = ['data'];
        form_counter = file_form_counter;
    }

    let insertFragment = document.getElementById(`${formset}_formset`);
    let total_input = document.createElement('input');
    total_input.type = 'hidden';
    total_input.name = `${formset}-TOTAL_FORMS`;
    total_input.value = `${form_counter}`;
    total_input.id = `id_${formset}-TOTAL_FORMS`;
    insertFragment.appendChild(total_input);

    for (let i = 0; i < parameters.length; i++) {
        let p = document.createElement('p');
        let label = document.createElement('label');
        let input = document.createElement('input');
        label.htmlFor = `id_${formset}-${form_counter-1}-` + parameters[i];
        label.innerHTML = `${ucFirst(parameters[i])}: `;

        if (formset === 'employer') {
            input.type = 'text';
            input.maxLength = 20;
        }
        else {
            input.type = 'file';
        }

        input.name = `${formset}-${form_counter-1}-` + parameters[i];
        input.id = `id_${formset}-${form_counter-1}-` + parameters[i];
        p.appendChild(label);
        p.appendChild(input);

        if (i === parameters.length - 1) {
            let hidden_input = document.createElement('input');
            hidden_input.type = 'hidden';
            hidden_input.name = `${formset}-${form_counter-1}-id`;
            hidden_input.id = `id_${formset}-${form_counter-1}-id`;
            p.appendChild(hidden_input)
        }
        insertFragment.appendChild(p);
    }
}