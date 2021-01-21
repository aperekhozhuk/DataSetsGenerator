function CreateNewSchemaForm() {
    let form = document.getElementById('newSchemaForm');
    let i = 0;

    const schema_field_name = "schema_name"
    let schema_name_element_label = document.createElement("label");
    schema_name_element_label.setAttribute("for", schema_field_name);
    schema_name_element_label.innerHTML = "Schema name";

    let schema_name_element = document.createElement("input");
    schema_name_element.setAttribute("type", "text");
    schema_name_element.setAttribute("required", "required");
    schema_name_element.setAttribute("name", schema_field_name);

    form.appendChild(schema_name_element_label);
    form.appendChild(schema_name_element);

    for (let [key1, value1] of Object.entries(new_schema_form_parameters)) {
        i++;
        // Creating fieldset element that holds column settings
        let fieldset_element = document.createElement("fieldset")
        // Creating order field
        let order_element_name = `column_${i}_order`;
        // Label
        let order_element_label = document.createElement("label");
        order_element_label.setAttribute("for", order_element_name);
        order_element_label.innerHTML = "Order:";
        // Input
        let order_element = document.createElement("input");
        order_element.setAttribute("name", order_element_name);
        order_element.setAttribute("type", "number");
        order_element.setAttribute("step", 1.0);
        order_element.setAttribute("required", "required");
        order_element.setAttribute("value", i);
        // Add to fieldset
        fieldset_element.appendChild(order_element_label);
        fieldset_element.appendChild(order_element);
        // Creating input field for columnt name
        // Creating Label
        let input_element_name = `column_${i}_name`;
        let input_element_label = document.createElement("label");
        input_element_label.setAttribute("for", input_element_name);
        input_element_label.innerHTML = "Column name:"
        // Creating input
        let input_element = document.createElement("input")
        input_element.setAttribute("value", key1);
        input_element.setAttribute("type", "text");
        input_element.setAttribute("required", "required")
        input_element.setAttribute("name", input_element_name);
        // Appending to fieldset
        fieldset_element.appendChild(input_element_label);
        fieldset_element.appendChild(input_element);

        // Creating dropdown list for selecting type of element
        // Creating Label
        let select_element_label = document.createElement("label");
        let select_element_name = `column_${i}_type`;
        select_element_label.setAttribute("for", select_element_name);
        select_element_label.innerHTML = "Type:";
        // Creating selector
        let select_element = document.createElement("select");
        select_element.setAttribute("name", select_element_name);
        // Creating select options for each Type
        for (let [key2, value2] of Object.entries(new_schema_form_parameters)) {
            let option_element = document.createElement("option");
            option_element.setAttribute("value", key2);
            option_element.innerHTML = key2;
            if (key2 == key1) {
                option_element.setAttribute("selected", "selected");
            }
            select_element.appendChild(option_element);
        }
        // Apending to fieldset
        fieldset_element.appendChild(select_element_label);
        fieldset_element.appendChild(select_element);
        // If element's type supports some parameters
        if (value1) {
            for (let [key2, value2] of Object.entries(value1)) {
                // Creating label
                let parameter_element_name = `column_${i}_${key2}`;
                let parameter_element_label = document.createElement("label");
                parameter_element_label.setAttribute("for", parameter_element_name);
                parameter_element_label.innerHTML = `${key2.toUpperCase()}:`;
                // Creating parameter's input element
                let parameter_element = document.createElement("input");
                parameter_element.setAttribute("required", "required")
                parameter_element.setAttribute("name", parameter_element_name);
                // Setting provided atributes
                for (let [key3, value3] of Object.entries(value2)) {
                    parameter_element.setAttribute(key3, value3);
                }
                // Adding to fieldset
                fieldset_element.appendChild(parameter_element_label);
                fieldset_element.appendChild(parameter_element);
            }
        }
        fieldset_element.appendChild(document.createElement("br"));
        // Apending fieldset to form
        form.appendChild(fieldset_element);
    }

    let submit_button = document.createElement("button");
    submit_button.setAttribute("type", "submit");
    submit_button.innerHTML = "Create Schema";
    form.appendChild(submit_button);
}

CreateNewSchemaForm();
