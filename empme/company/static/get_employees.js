function getEmployeesForCompany(company_id) {
    $.ajax({
        url: '/companies/get_employees/',
        data: { 'company_id': company_id },
        dataType: 'json',
        success: function (data) {
            var employees = data.employees;
            var employeesField = $('#id_assigned_employees');
            employeesField.empty();
            $.each(employees, function (index, employee) {
                employeesField.append($('<option>', {
                    value: employee.id,
                    text: employee.name
                }));
            });
        }
    });
}
