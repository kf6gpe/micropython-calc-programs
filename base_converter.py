def bc():
    """REPL-style base converter for binary, octal, decimal, and hexadecimal"""
    print("Base Converter - Enter number base (e.g., 1010 2 or FF 16)")
    print("Supported bases: 2 (binary), 8 (octal), 10 (decimal), 16 (hexadecimal)")
    print("Press Ctrl+C to exit\n")

    while True:
        try:
            # Prompt user
            user_input = input("> ").strip()

            if not user_input:
                continue

            # Parse input
            parts = user_input.split()
            if len(parts) != 2:
                print("Error: Use format number base (e.g., 1010 2)")
                continue

            number_str, base_str = parts
            number_str = number_str.strip()
            base_str = base_str.strip()

            # Validate base
            try:
                base = int(base_str)
            except ValueError:
                print("Error: Base must be a number")
                continue

            if base not in [2, 8, 10, 16]:
                print("Error: Base must be 2, 8, 10, or 16")
                continue

            # Convert to decimal
            try:
                decimal_value = int(number_str, base)
            except ValueError:
                print(f"Error: Invalid number for base {base}")
                continue

            # Display in all bases
            print(f"Binary:      {bin(decimal_value)}")
            print(f"Octal:       {oct(decimal_value)}")
            print(f"Decimal:     {decimal_value}")
            print(f"Hexadecimal: {hex(decimal_value)}")
            print()

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            print("\nExiting...")
            break

# Run bc() to start the converter
