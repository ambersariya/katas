package com.github.ambersariya.unit.booking;

import com.github.ambersariya.booking.CompanyPolicy;
import com.github.ambersariya.booking.EmployeePolicy;
import com.github.ambersariya.booking.InMemoryBookingPolicyRepository;
import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.core.EmployeeId;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

public class InMemoryBookingPolicyRepositoryShould {
    private static final CompanyId COMPANY_ID = new CompanyId("5c02072a-1a2e-4731-86e2-ef18859ddfb6");
    private static final EmployeeId EMPLOYEE_ID =  new EmployeeId("a3a42ad5-8610-4d63-81a8-44915281332c");
    private static final List<RoomType> COMPANY_ROOM_TYPES = List.of(RoomType.STANDARD);
    private static final List<RoomType> EMPLOYEE_ROOM_TYPES = List.of(RoomType.STANDARD, RoomType.JUNIOR_SUITE);
    private static final CompanyPolicy COMPANY_POLICY = new CompanyPolicy(COMPANY_ID, COMPANY_ROOM_TYPES);
    private static final EmployeePolicy EMPLOYEE_POLICY = new EmployeePolicy(EMPLOYEE_ID, EMPLOYEE_ROOM_TYPES);
    private InMemoryBookingPolicyRepository bookingPolicyRepository;

    @BeforeEach
    public void setUp() {
        bookingPolicyRepository = new InMemoryBookingPolicyRepository();
    }

    @Test
    public void find_a_company_booking_policy_by_id() {
        bookingPolicyRepository.save(COMPANY_POLICY);
        var result = bookingPolicyRepository.findCompanyPolicyBy(COMPANY_ID);

        assertEquals(COMPANY_POLICY, result);
    }

    @Test
    public void find_an_employee_policy_by_id() {
        bookingPolicyRepository.save(EMPLOYEE_POLICY);
        var result = bookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID);

        assertEquals(EMPLOYEE_POLICY, result);
    }

    @Test
    public void throw_exception_when_company_policy_doesnt_exist() {
        assertNull(bookingPolicyRepository.findCompanyPolicyBy(COMPANY_ID));
    }

    @Test
    public void throw_exception_when_employee_policy_doesnt_exist() {
        assertNull(bookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID));
    }

    @Test
    public void update_existing_company_policy_with_junior_suite_room_type() {
        bookingPolicyRepository.save(COMPANY_POLICY);
        var updatedPolicy = new CompanyPolicy(COMPANY_ID, List.of(RoomType.STANDARD, RoomType.JUNIOR_SUITE));
        bookingPolicyRepository.save(updatedPolicy);

        var result = bookingPolicyRepository.findCompanyPolicyBy(COMPANY_ID);
        assertEquals(updatedPolicy, result);
    }

    @Test
    public void update_existing_employee_policy_with_master_suite_room_type() {
        bookingPolicyRepository.save(EMPLOYEE_POLICY);
        var updatedPolicy = new EmployeePolicy(
                EMPLOYEE_ID,
                List.of(RoomType.STANDARD, RoomType.JUNIOR_SUITE, RoomType.MASTER_SUITE)
        );
        bookingPolicyRepository.save(updatedPolicy);

        var result = bookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID);
        assertEquals(updatedPolicy, result);
    }
}
