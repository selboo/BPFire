#!/usr/bin/perl
###############################################################################
#                                                                             #
# IPFire.org - A linux based firewall                                         #
# Copyright (C) 2011  IPFire Team  <info@ipfire.org>                          #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by        #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
###############################################################################

use strict;

# enable only the following on debugging purpose
#use warnings;
#use CGI::Carp 'fatalsToBrowser';

require '/var/ipfire/general-functions.pl';
require "${General::swroot}/lang.pl";
require "${General::swroot}/header.pl";

&Header::showhttpheaders();

&Header::openpage($Lang::tr{'credits'}, 1, '');

&Header::openbigbox('100%', 'center');

&Header::openbox('100%', 'left', $Lang::tr{'donation'});

print <<END
<p>$Lang::tr{'donation-bpfire-text'}</p>
<div align="center">
        <a href="https://www.paypal.com/donate/?business=BL97G8687E5B6&no_recurring=0&item_name=Make+revolutionary+eBPF+technology+available+for+non-tech+savvy+users+for+safe+online+surfing&currency_code=USD" target="_blank">
                <strong>$Lang::tr{'donation-bpfire'}</strong>
        </a>
</div>
<p>$Lang::tr{'donation-ipfire-text'}</p>
<div align="center">

	<a href="https://www.ipfire.org/donate" target="_blank">
		<strong>$Lang::tr{'donation-ipfire'}</strong>
	</a>
</div>
END
;
&Header::closebox();

&Header::openbox('100%', 'left',);

print <<END
<br>
<center>
	$Lang::tr{'visit us at'}: <b><a href='http://www.bpfire.net/' target="_blank">https://www.bpfire.net/</a></b> <b><a href='https://www.ipfire.org/' target="_blank">https://www.ipfire.org/</a></b>
</center>
<br><br>

<p>
	<!-- CONTRIBUTORS -->
Michael Tremer,
Arne Fitzenreiter,
Peter Müller,
Adolf Belka,
Stefan Schantl,
Matthias Fischer,
Christian Schmidt,
Alexander Marx,
Erik Kapfer,
Jonatan Schlag,
Jan Paul Tücking,
Dirk Wagner,
Marcel Lorenz,
Leo-Andres Hofmann,
Alf Høgemark,
Timo Eissler,
Ben Schweikert,
Daniel Weismüller,
Peter Pfeiffer,
Robin Roevens,
Daniel Glanzmann,
Heiner Schmeling,
Stephan Feddersen,
Stéphane Pautrel,
Jon Murphy,
Tim FitzGeorge,
Jan Lentfer,
Marcus Scholz,
Ersan Yildirim,
Jörn-Ingo Weigert,
Alexander Koch,
Wolfgang Apolinarski,
Alfred Haas,
Lars Schuhmacher,
Rene Zingel,
Sascha Kilian,
Bernhard Bitsch,
Ronald Wiesinger,
Florian Bührle,
Justin Luth,
Mathew McBride,
Michael Eitelwein,
Rob Brewer,
Alex Koch,
Dominik Hassler,
Larsen,
Ramax Lo,
Gabriel Rolland,
Marcel Follert,
Anton D. Seliverstov,
Bernhard Bittner,
Daniel Weismueller,
David Kleuker,
Hans Horsten,
Jakub Ratajczak,
Jorrit de Jonge,
Przemek Zdroik,
Roberto Peña,
Sebastien GISLAIN,
Alexander Rudolf Gruber,
Andrew Bellows,
Axel Gembe,
Bernhard Held,
Christoph Anderegg,
Daniel Aleksandersen,
Douglas Duckworth,
Eberhard Beilharz,
Ersan Yildirim Ersan,
Gerd Hoerst,
Giovanni Aneloni,
H. Horsten,
Heino Gutschmidt,
Jan Behrens,
Jochen Kauz,
Julian McConnell,
Kay-Michael Köhler,
Kim Wölfel,
Logan Schmidt,
Markus Untersee,
Nico Prenzel,
Oliver Fuhrer,
Osmar Gonzalez,
Paul T. Simmons,
Robert Möker,
Stefan Ernst,
Stefan Ferstl,
Steffen Klammer,
Thomas Cekal,
Thomas Ebert,
Timmothy Wilson,
Umberto Parma
	<!-- END -->
</p>
END
;
&Header::closebox();

&Header::closebigbox();

&Header::closepage();
