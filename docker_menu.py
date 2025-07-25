import os
while True:
        print (
        """
        ---------------------------------------------------------------
                       Docker Menu Driven Program
        ---------------------------------------------------------------
        1. Display all locally available Images
        2. Pull Image from Docker Hub
        3. Display all Containers
        4. Launch New Container
        5. Start Container
        6. Stop Container
        7. Remove Container
        8. Exit

        -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                                                        -by Rohan Kasabe

        """
        )

        choice = input("Please enter your choice => ")

        if choice == "1":
                os.system(f"docker images")

        elif choice == "2":
                image = input ("Which OS image and version you want to pull e.g. ubuntu:14.04 => ")
                os.system(f"docker pull {image}")

        elif choice == "3":
                os.system(f"docker ps -a")

        elif choice == "4":
                image = input("Which OS image you want to use => ")
                name = input("What name you want to give for this container =>  ")
                os.system(f"docker run -dit  --name{name} {image} ")

        elif choice == "5":
                name = input("What container you want to start can you provide me container name =>  ")
                os.system(f"docker start {name} ")

        elif choice == "6":
                name = input("What container you want to stop can you provide me container name =>  ")
                os.system(f"docker stop {name} ")

        elif choice == "7":
                name = input("What container you want to remove can you provide me container name =>  ")
                os.system(f"docker rm -f {name} ")

        elif choice == "8":
                break

        else:
                print("Please give proper Input!")
