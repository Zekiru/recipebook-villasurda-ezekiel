function addRow(type) {
    const list = document.getElementById(`${type}-list`);
    const totalForms = document.getElementById(`id_${type}s-TOTAL_FORMS`);
    const count = parseInt(totalForms.value);
    
    let newRow = document.getElementById(`${type}-empty`).innerHTML;
    newRow = newRow.replace(/__prefix__/g, count);
    
    list.insertAdjacentHTML('beforeend', newRow);
    totalForms.value = count + 1;
}

function removeRow(btn) {
    const row = btn.closest('.formset-row');
    const deleteCheckbox = row.querySelector('input[name$="-DELETE"]');

    if (deleteCheckbox) {
        deleteCheckbox.checked = true;
        row.style.display = 'none';
    } else {
        row.remove();
    }
}

document.querySelectorAll('.remove-btn').forEach(btn => {
    btn.addEventListener('click', function() { removeRow(this); });
});