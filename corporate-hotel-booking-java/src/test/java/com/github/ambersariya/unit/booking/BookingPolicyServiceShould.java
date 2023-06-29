package com.github.ambersariya.unit.booking;

import com.github.ambersariya.booking.BookingPolicyRepository;
import com.github.ambersariya.booking.BookingPolicyService;
import com.github.ambersariya.booking.CompanyPolicy;
import com.github.ambersariya.booking.EmployeePolicy;
import com.github.ambersariya.core.CompanyId;
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
    private static final CompanyId COMPANY_ID = new CompanyId("5c02072a-1a2e-4731-86e2-ef18859ddfb6");
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

        verify(companyBookingPolicyRepository).save(companyPolicy);
    }

    @Test
    public void allow_saving_employee_policy() {
        var employeeRoomTypes = List.of(RoomType.JUNIOR_SUITE);
        var employeePolicy = new EmployeePolicy(EMPLOYEE_ID, employeeRoomTypes);

        bookingPolicyService.setEmployeePolicy(EMPLOYEE_ID, employeeRoomTypes);

        verify(companyBookingPolicyRepository).save(employeePolicy);
    }

    @Test
    public void allow_booking_a_standard_room_on_company_policy() {
        var companyRoomTypes = List.of(RoomType.STANDARD);
        var companyPolicy = new CompanyPolicy(COMPANY_ID, companyRoomTypes);
        when(employeeRepository.findById(EMPLOYEE_ID)).thenReturn(EMPLOYEE);
        when(companyBookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID)).thenReturn(null);
        when(companyBookingPolicyRepository.findCompanyPolicyBy(COMPANY_ID)).thenReturn(companyPolicy);

        assertTrue(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.STANDARD));
    }

    @Test
    public void allow_booking_a_junior_suite_room_on_employee_policy() {
        var employeePolicy = new EmployeePolicy(EMPLOYEE_ID, List.of(RoomType.JUNIOR_SUITE));

        when(companyBookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID)).thenReturn(employeePolicy);

        assertTrue(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.JUNIOR_SUITE));
    }

    @Test
    public void allow_booking_any_room_when_no_policies_exist() {

        when(employeeRepository.findById(EMPLOYEE_ID)).thenReturn(EMPLOYEE);
        when(companyBookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID)).thenReturn(null);
        when(companyBookingPolicyRepository.findCompanyPolicyBy(COMPANY_ID)).thenReturn(null);

        assertTrue(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.JUNIOR_SUITE));
    }
}
