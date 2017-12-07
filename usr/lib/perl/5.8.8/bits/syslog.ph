require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&_SYS_SYSLOG_H)) {
    die("Never include <bits/syslog.h> directly; use <sys/syslog.h> instead.");
}
unless(defined(&syslog)) {
    sub syslog () {	( &pri, ...)  &__syslog_chk ( &pri,  &__USE_FORTIFY_LEVEL - 1,  &__VA_ARGS__);}
}
if(defined(&__USE_BSD)) {
    eval 'sub vsyslog {
        my($pri, $fmt, $ap) = @_;
	    eval q( &__vsyslog_chk ($pri,  &__USE_FORTIFY_LEVEL - 1, $fmt, $ap));
    }' unless defined(&vsyslog);
}
1;
