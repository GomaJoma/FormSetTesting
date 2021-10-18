"use strict";
let form_counter = 1;
let employer_form_counter = 2;
let file_form_counter = 1;

function GetInsertPosition(formset) {
    return document.getElementById(`${formset}_formset`);
}

function InsertTotalFormNum(formset, form_counter) {
    let insertPosition = GetInsertPosition(formset);
    let total_input = document.createElement('input');
    total_input.type = 'hidden';
    total_input.name = `${formset}-TOTAL_FORMS`;
    total_input.value = `${form_counter}`;
    total_input.id = `id_${formset}-TOTAL_FORMS`;
    insertPosition.appendChild(total_input);
}

function ucFirst(str) {
  if (!str) return str;

  return str[0].toUpperCase() + str.slice(1);
}

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

    InsertTotalFormNum(formset, form_counter);

    for (let i = 0; i < parameters.length; i++) {
        let p = document.createElement('p');
        let label = document.createElement('label');
        let input = document.createElement('input');
        p.id = `${formset}-${form_counter-1}`;
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
        let insertPosition = GetInsertPosition(formset);
        insertPosition.appendChild(p);
    }
}
function delete_item(formset) {
    if (formset === 'employer') {
                employer_form_counter--;

        form_counter = employer_form_counter;
    }
    else if (formset === 'file') {
                file_form_counter--;

        form_counter = file_form_counter;
    }

    let nested_node = document.getElementById(`${formset}-${form_counter}`);
    if (nested_node.parentNode) {
      nested_node.parentNode.removeChild(nested_node);
    }
    if (form_counter === 1) {
        InsertTotalFormNum(formset, form_counter);
    }
}