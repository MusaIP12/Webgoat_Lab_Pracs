CREATE TABLE employees (
    userid INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    auth_tan VARCHAR(10)
);

INSERT INTO employees (userid, first_name, last_name, department, salary, auth_tan) VALUES
(32147, 'Paulina', 'Travers', 'Accounting', 46000.00, 'P45JSI'),
(89762, 'Tobi', 'Barnett', 'Development', 77000.00, 'TA9LL1'),
(96134, 'Bob', 'Franco', 'Marketing', 83700.00, 'LO9S2V'),
(34477, 'Abraham', 'Holman', 'Development', 50000.00, 'UU2ALK'),
(37648, 'John', 'Smith', 'Marketing', 64350.00, '3SL99A');

SELECT first_name, last_name FROM employees;

INSERT INTO employees ( userid, first_name, last_name, department, salary , auth_tan) VALUES ( 12300, 'James', 'Cole', 'Education', '48000', 'SC23900');

UPDATE employees SET department = 'Development' WHERE first_name = 'Tobi' AND last_name = 'Barnett';

UPDATE employees SET department = 'Sales' WHERE userid = 89762;

ALTER TABLE employees ADD COLUMN phone VARCHAR(20);

-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.
-- To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.	0.016 sec
