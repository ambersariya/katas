package com.github.ambersariya.employee;

import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.core.EmployeeId;

public record Employee(EmployeeId employeeId, CompanyId companyId) {
}
