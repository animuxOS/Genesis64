require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&__ARCH_I386_IOCTLS_H__)) {
    eval 'sub __ARCH_I386_IOCTLS_H__ () {1;}' unless defined(&__ARCH_I386_IOCTLS_H__);
    require 'asm/ioctl.ph';
    eval 'sub TCGETS () {0x5401;}' unless defined(&TCGETS);
    eval 'sub TCSETS () {0x5402;}' unless defined(&TCSETS);
    eval 'sub TCSETSW () {0x5403;}' unless defined(&TCSETSW);
    eval 'sub TCSETSF () {0x5404;}' unless defined(&TCSETSF);
    eval 'sub TCGETA () {0x5405;}' unless defined(&TCGETA);
    eval 'sub TCSETA () {0x5406;}' unless defined(&TCSETA);
    eval 'sub TCSETAW () {0x5407;}' unless defined(&TCSETAW);
    eval 'sub TCSETAF () {0x5408;}' unless defined(&TCSETAF);
    eval 'sub TCSBRK () {0x5409;}' unless defined(&TCSBRK);
    eval 'sub TCXONC () {0x540a;}' unless defined(&TCXONC);
    eval 'sub TCFLSH () {0x540b;}' unless defined(&TCFLSH);
    eval 'sub TIOCEXCL () {0x540c;}' unless defined(&TIOCEXCL);
    eval 'sub TIOCNXCL () {0x540d;}' unless defined(&TIOCNXCL);
    eval 'sub TIOCSCTTY () {0x540e;}' unless defined(&TIOCSCTTY);
    eval 'sub TIOCGPGRP () {0x540f;}' unless defined(&TIOCGPGRP);
    eval 'sub TIOCSPGRP () {0x5410;}' unless defined(&TIOCSPGRP);
    eval 'sub TIOCOUTQ () {0x5411;}' unless defined(&TIOCOUTQ);
    eval 'sub TIOCSTI () {0x5412;}' unless defined(&TIOCSTI);
    eval 'sub TIOCGWINSZ () {0x5413;}' unless defined(&TIOCGWINSZ);
    eval 'sub TIOCSWINSZ () {0x5414;}' unless defined(&TIOCSWINSZ);
    eval 'sub TIOCMGET () {0x5415;}' unless defined(&TIOCMGET);
    eval 'sub TIOCMBIS () {0x5416;}' unless defined(&TIOCMBIS);
    eval 'sub TIOCMBIC () {0x5417;}' unless defined(&TIOCMBIC);
    eval 'sub TIOCMSET () {0x5418;}' unless defined(&TIOCMSET);
    eval 'sub TIOCGSOFTCAR () {0x5419;}' unless defined(&TIOCGSOFTCAR);
    eval 'sub TIOCSSOFTCAR () {0x541a;}' unless defined(&TIOCSSOFTCAR);
    eval 'sub FIONREAD () {0x541b;}' unless defined(&FIONREAD);
    eval 'sub TIOCINQ () { &FIONREAD;}' unless defined(&TIOCINQ);
    eval 'sub TIOCLINUX () {0x541c;}' unless defined(&TIOCLINUX);
    eval 'sub TIOCCONS () {0x541d;}' unless defined(&TIOCCONS);
    eval 'sub TIOCGSERIAL () {0x541e;}' unless defined(&TIOCGSERIAL);
    eval 'sub TIOCSSERIAL () {0x541f;}' unless defined(&TIOCSSERIAL);
    eval 'sub TIOCPKT () {0x5420;}' unless defined(&TIOCPKT);
    eval 'sub FIONBIO () {0x5421;}' unless defined(&FIONBIO);
    eval 'sub TIOCNOTTY () {0x5422;}' unless defined(&TIOCNOTTY);
    eval 'sub TIOCSETD () {0x5423;}' unless defined(&TIOCSETD);
    eval 'sub TIOCGETD () {0x5424;}' unless defined(&TIOCGETD);
    eval 'sub TCSBRKP () {0x5425;}' unless defined(&TCSBRKP);
    eval 'sub TIOCSBRK () {0x5427;}' unless defined(&TIOCSBRK);
    eval 'sub TIOCCBRK () {0x5428;}' unless defined(&TIOCCBRK);
    eval 'sub TIOCGSID () {0x5429;}' unless defined(&TIOCGSID);
    eval 'sub TCGETS2 () { &_IOR(ord(\'T\'),0x2a, 1;}' unless defined(&TCGETS2);
    eval 'sub TCSETS2 () { &_IOW(ord(\'T\'),0x2b, 1;}' unless defined(&TCSETS2);
    eval 'sub TCSETSW2 () { &_IOW(ord(\'T\'),0x2c, 1;}' unless defined(&TCSETSW2);
    eval 'sub TCSETSF2 () { &_IOW(ord(\'T\'),0x2d, 1;}' unless defined(&TCSETSF2);
    eval 'sub TIOCGPTN () { &_IOR(ord(\'T\'),0x30, \'unsigned int\');}' unless defined(&TIOCGPTN);
    eval 'sub TIOCSPTLCK () { &_IOW(ord(\'T\'),0x31, \'int\');}' unless defined(&TIOCSPTLCK);
    eval 'sub FIONCLEX () {0x5450;}' unless defined(&FIONCLEX);
    eval 'sub FIOCLEX () {0x5451;}' unless defined(&FIOCLEX);
    eval 'sub FIOASYNC () {0x5452;}' unless defined(&FIOASYNC);
    eval 'sub TIOCSERCONFIG () {0x5453;}' unless defined(&TIOCSERCONFIG);
    eval 'sub TIOCSERGWILD () {0x5454;}' unless defined(&TIOCSERGWILD);
    eval 'sub TIOCSERSWILD () {0x5455;}' unless defined(&TIOCSERSWILD);
    eval 'sub TIOCGLCKTRMIOS () {0x5456;}' unless defined(&TIOCGLCKTRMIOS);
    eval 'sub TIOCSLCKTRMIOS () {0x5457;}' unless defined(&TIOCSLCKTRMIOS);
    eval 'sub TIOCSERGSTRUCT () {0x5458;}' unless defined(&TIOCSERGSTRUCT);
    eval 'sub TIOCSERGETLSR () {0x5459;}' unless defined(&TIOCSERGETLSR);
    eval 'sub TIOCSERGETMULTI () {0x545a;}' unless defined(&TIOCSERGETMULTI);
    eval 'sub TIOCSERSETMULTI () {0x545b;}' unless defined(&TIOCSERSETMULTI);
    eval 'sub TIOCMIWAIT () {0x545c;}' unless defined(&TIOCMIWAIT);
    eval 'sub TIOCGICOUNT () {0x545d;}' unless defined(&TIOCGICOUNT);
    eval 'sub TIOCGHAYESESP () {0x545e;}' unless defined(&TIOCGHAYESESP);
    eval 'sub TIOCSHAYESESP () {0x545f;}' unless defined(&TIOCSHAYESESP);
    eval 'sub FIOQSIZE () {0x5460;}' unless defined(&FIOQSIZE);
    eval 'sub TIOCPKT_DATA () {0;}' unless defined(&TIOCPKT_DATA);
    eval 'sub TIOCPKT_FLUSHREAD () {1;}' unless defined(&TIOCPKT_FLUSHREAD);
    eval 'sub TIOCPKT_FLUSHWRITE () {2;}' unless defined(&TIOCPKT_FLUSHWRITE);
    eval 'sub TIOCPKT_STOP () {4;}' unless defined(&TIOCPKT_STOP);
    eval 'sub TIOCPKT_START () {8;}' unless defined(&TIOCPKT_START);
    eval 'sub TIOCPKT_NOSTOP () {16;}' unless defined(&TIOCPKT_NOSTOP);
    eval 'sub TIOCPKT_DOSTOP () {32;}' unless defined(&TIOCPKT_DOSTOP);
    eval 'sub TIOCSER_TEMT () {0x1;}' unless defined(&TIOCSER_TEMT);
}
1;
