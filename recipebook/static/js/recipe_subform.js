function addRow(name) {
    const totalForms = document.getElementById(`id_${name}-TOTAL_FORMS`);
    const container = document.getElementById(`${name}-list`);
    const emptyRowElement = document.getElementById(`${name}-empty`);

    const currentCount = parseInt(totalForms.value);
    const newRowHtml = emptyRowElement.innerHTML.replace(/__prefix__/g, currentCount);

    container.insertAdjacentHTML('beforeend', newRowHtml);
    totalForms.value = currentCount + 1;
}

function removeRowImage(btn) {
    const row = btn.closest('.formset-row');
    const container = document.getElementById('image-list');
    const totalForms = document.getElementById('id_image-TOTAL_FORMS');
    
    row.remove();
    
    const remainingRows = container.querySelectorAll('.image-form');
    totalForms.value = remainingRows.length;

    remainingRows.forEach((r, index) => {
        r.querySelectorAll('input, select, textarea, label').forEach(el => {
            if (el.name) el.name = el.name.replace(/image-\d+-/, `image-${index}-`);
            if (el.id) el.id = el.id.replace(/id_image-\d+-/, `id_image-${index}-`);
            if (el.getAttribute('for')) el.setAttribute('for', el.getAttribute('for').replace(/id_image-\d+-/, `id_image-${index}-`));
        });
    });
}

function removeRowIngredient(btn) {
    const row = btn.closest('.formset-row');
    const container = document.getElementById('ingredient-list');
    const totalForms = document.getElementById('id_ingredient-TOTAL_FORMS');
    
    row.remove();
    
    const remainingRows = container.querySelectorAll('.ingredient-form');
    totalForms.value = remainingRows.length;

    remainingRows.forEach((r, index) => {
        r.querySelectorAll('input, select, textarea, label').forEach(el => {
            if (el.name) el.name = el.name.replace(/ingredient-\d+-/, `ingredient-${index}-`);
            if (el.id) el.id = el.id.replace(/id_ingredient-\d+-/, `id_ingredient-${index}-`);
            if (el.getAttribute('for')) el.setAttribute('for', el.getAttribute('for').replace(/id_ingredient-\d+-/, `id_ingredient-${index}-`));
        });
    });
}
