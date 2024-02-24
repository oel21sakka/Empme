function getDepartmentsForCompany(company_id) {
    $.ajax({
        url: '/companies/get_departments/',
        data: { 'company_id': company_id },
        dataType: 'json',
        success: function (data) {
            var departments = data.departments;
            console.log(data)
            var departmentField = $('#id_department');
            departmentField.empty();
            $.each(departments, function (index, department) {
                departmentField.append($('<option>', {
                    value: department.id,
                    text: department.name
                }));
            });
        }
    });
}
