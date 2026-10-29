import os


def move_file(command: str) -> None:
    split_command: list[str] = command.strip().split(" ")

    if (
        len(split_command) != 3
        or split_command[0] != "mv"
        or split_command[1] == ""
        or split_command[2] == ""
    ):
        return

    source_file_name: str = split_command[1]
    destination_file_name: str = split_command[2]

    if destination_file_name.endswith(("/", "\\")):
        os.makedirs(destination_file_name, exist_ok=True)
        destination_file_name = os.path.join(
            destination_file_name,
            os.path.basename(source_file_name)
        )
    else:
        dir_path = os.path.dirname(destination_file_name)

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    try:
        with (
            open(source_file_name, "r") as file_in,
            open(destination_file_name, "w") as file_out
        ):
            file_out.write(file_in.read())

    except FileNotFoundError:
        return

    else:
        os.remove(source_file_name)
