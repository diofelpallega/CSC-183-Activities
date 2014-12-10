Feature: Tool for accessing web resources using
	 HTTP or FTP protocol.

	 I want to access web resources using HTTP or FTP protocol

	 Scenario: Get web resources on http
	 Given I have the following web resources:
	 	 |   web_resources   |
	 	 |	www.ubuntu.com	 |
	 	 |	www.redhat.com	 |
	 	 |	www.suse.com	 |
	 	 |	www.maldrake.com |
     And I have my "localhost" as my domain
	 When I run the tool
	 Then I see the resources:
	 	 |   web_resources   |
	 	 |	www.ubuntu.com	 |
	 	 |	www.redhat.com	 |
	 	 |	www.suse.com	 |
	 	 |	www.maldrake.com |

	 Scenario: Get web resources on ftp
	 Given I freeBsd has this following web resources: 
         |     web_resources                                                 |
         |     CERT															              |
         |     CTM -> development/CTM										           |
         |     CVSup -> development/CVSup									           |
         |     ERRATA														              |
         |     ISO-IMAGES-amd64 -> releases/amd64/amd64/ISO-IMAGES 			  |
         |     ISO-IMAGES-i386 -> releases/i386/i386/ISO-IMAGES 			     |
         |     ISO-IMAGES-ia64 -> releases/ia64/ia64/ISO-IMAGES              |
         |     ISO-IMAGES-pc98 -> releases/pc98/ISO-IMAGES                   |
         |     ISO-IMAGES-powerpc -> releases/powerpc/powerpc/ISO-IMAGES     |
         |     ISO-IMAGES-powerpc64 -> releases/powerpc/powerpc64/ISO-IMAGES |
         |     ISO-IMAGES-sparc64 -> releases/sparc64/sparc64/ISO-IMAGES     |
         |     README.TXT													              |
         |     TIMESTAMP													              |
         |     branches														              |
         |     development                                                   |
         |     dir.sizes       												           |
         |     distfiles -> ports/distfiles									        |
         |     doc															              |
         |     ports														                 |
         |     releases														              |
         |     snapshots													              |
         |     tools														                 |
         |     updates 														              |

     And I have my "ftp.freebsd.org" as my domain
	  When I run the tool for ftp
	  Then I see the resources for ftp: 
         |     web_resources                                                 |
         |     CERT                                                          |
         |     CTM -> development/CTM                                        |
         |     CVSup -> development/CVSup                                    |
         |     ERRATA                                                        |
         |     ISO-IMAGES-amd64 -> releases/amd64/amd64/ISO-IMAGES           |
         |     ISO-IMAGES-i386 -> releases/i386/i386/ISO-IMAGES              |
         |     ISO-IMAGES-ia64 -> releases/ia64/ia64/ISO-IMAGES              |
         |     ISO-IMAGES-pc98 -> releases/pc98/ISO-IMAGES                   |
         |     ISO-IMAGES-powerpc -> releases/powerpc/powerpc/ISO-IMAGES     |
         |     ISO-IMAGES-powerpc64 -> releases/powerpc/powerpc64/ISO-IMAGES |
         |     ISO-IMAGES-sparc64 -> releases/sparc64/sparc64/ISO-IMAGES     |
         |     README.TXT                                                    |
         |     TIMESTAMP                                                     |
         |     branches                                                      |
         |     development                                                   |
         |     dir.sizes                                                     |
         |     distfiles -> ports/distfiles                                  |
         |     doc                                                           |
         |     ports                                                         |
         |     releases                                                      |
         |     snapshots                                                     |
         |     tools                                                         |
         |     updates                                                       |


