FROM postgres:13

CMD [ \
  "postgres", \
  "-c", "log_statement=all",\
  "-c", "log_checkpoints=on",\
  "-c", "log_line_prefix=%i@%d:[%p]:", \
  "-c", "log_min_duration_statement=1",\
  "-c", "log_connections=on",\
  "-c", "log_disconnections=on",\
  "-c", "log_lock_waits=on",\
  "-c", "log_temp_files=0",\
  "-c", "log_autovacuum_min_duration=0",\
  "-c", "log_error_verbosity=default",\
  "-c", "lc_messages=en_US.UTF-8" \
]