# Base Converter for TI Nspire CAS II
# Run this script from the Python app

def bc():
    """REPL-style base converter for binary, octal, decimal, and hexadecimal"""
    print("Base Converter")
    print("Format: number base")
    print("Example: 1010 2 or FF 16")
    print("Bases: 2, 8, 10, 16")
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
                print("Error: Use number base")
                continue

            number_str = parts[0].strip()
            base_str = parts[1].strip()

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
                print("Error: '" + number_str + "' is not a valid base " + str(base) + " number")
                continue

            # Display in all bases
            print("Binary:      " + bin(decimal_value))
            print("Octal:       " + oct(decimal_value))
            print("Decimal:     " + str(decimal_value))
            print("Hexadecimal: " + hex(decimal_value))
            print()

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            print("\nExiting...")
            break
        except:
            print("Error occurred")
            continue

# Run bc() to start the converter
