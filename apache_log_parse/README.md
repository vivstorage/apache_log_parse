Support only python 2.7, maybe 3 too, but not tested, there is 2 additional module files included,
they should be in 1 dir with original script

python2.7 apache_log_parse2.py --help
usage: apache_log_parse2.py [-h] [--l string] [--tr10 TR10] [--tip10 TIP10]
                            [--tf10 TF10] [--pf PF] [--ps PS]

optional arguments:
  -h, --help     show this help message and exit
  --l string     log file path
  --tr10 TR10    top 10 requests
  --tip10 TIP10  top 10 ips
  --tf10 TF10    top 10 fail requests
  --pf PF        Percent of fail requests
  --ps PS        Percent of successfull requests
  
  
example of run, there is strang behaviour of python 2 which ask for argument after all flags, on 3 version there is no need it,
and script should run like  
python2.7 apache_log_parse2.py --l apache-httpd.log --tr10 1
Top 10 requests:

('/printer/remove.php', 556)
('/statistics/list.php', 533)
('/printer/search.php', 529)
('/main/call.php', 524)
('/finance/add.php', 524)
('/printer/list.php', 522)
('/system/list.php', 520)
('/system/call.php', 516)
('/kernel/get.php', 510)
('/kernel/call.php', 509)
('/finance/call.php', 509)