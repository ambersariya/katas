package com.github.ambersariya.unit.booking;

import com.github.ambersariya.booking.*;
import com.github.ambersariya.employee.Employee;
import com.github.ambersariya.employee.EmployeeRepository;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class BookingPolicyServiceShould {
    private static final int COMPANY_ID = 1;
    private static final int EMPLOYEE_ID = 1;
    private static final Employee EMPLOYEE = new Employee(EMPLOYEE_ID, COMPANY_ID);
    @Mock
    private BookingPolicyRepository companyBookingPolicyRepository;
    @Mock
    private EmployeeRepository employeeRepository;
    private BookingPolicyService bookingPolicyService;

    @BeforeEach
    public void setUp() {
        bookingPolicyService = new BookingPolicyService(companyBookingPolicyRepository, employeeRepository);
    }

    @Test
    public void allow_saving_company_policy() {
        var companyRoomTypes = List.of(RoomType.STANDARD);
        var companyPolicy = new CompanyPolicy(COMPANY_ID, companyRoomTypes);

        bookingPolicyService.setCompanyPolicy(COMPANY_ID, companyRoomTypes);

        verify(companyBookingPolicyRepository).saveCompanyPolicy(companyPolicy);
    }

    @Test
    public void allow_saving_employee_policy() {
        var employeeRoomTypes = List.of(RoomType.JUNIOR_SUITE);
        var employeePolicy = new EmployeePolicy(EMPLOYEE_ID, employeeRoomTypes);

        bookingPolicyService.setEmployeePolicy(EMPLOYEE_ID, employeeRoomTypes);

        verify(companyBookingPolicyRepository).saveEmployeePolicy(employeePolicy);
    }

    @Test
    public void allow_booking_a_standard_room_on_company_policy() {
        var companyRoomTypes = List.of(RoomType.STANDARD);
        var companyPolicy = new CompanyPolicy(COMPANY_ID, companyRoomTypes);

        when(companyBookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID)).thenThrow(EmployeeBookingPolicyNotFound.class);
        when(employeeRepository.findById(EMPLOYEE_ID)).thenReturn(EMPLOYEE);
        when(companyBookingPolicyRepository.findCompanyPolicyBy(COMPANY_ID)).thenReturn(companyPolicy);

        assertTrue(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.STANDARD));
    }
}
