import unittest
from unittest.mock import Mock, patch
from src.fifa import Fifa


class TestGetMasterData(unittest.TestCase):
    @patch('src.fifa.requests.get')
    def test_get_master_data(self, mock_get):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.content = """
            <html>
                <h3>
                    <span class="mw-headline" id="Brazil">Brazil</span>
                    <span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=2022_FIFA_World_Cup_squads&amp;action=edit&amp;section=32" title="Edit section: Brazil">edit</a><span class="mw-editsection-bracket">]</span></span>
                </h3>
                <div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg" class="image"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg/220px-Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg" decoding="async" width="220" height="153" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg/330px-Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg/440px-Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg 2x" data-file-width="800" data-file-height="557"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Brazil_vs_Serbia_World_Cup_2022_match_Brazil_line-up.jpg" class="internal" title="Enlarge"></a></div>The Brazil starting XI for their first group match</div></div></div>
                <p>Coach: <a href="/wiki/Tite_(football_manager)" title="Tite (football manager)">Tite</a>
                </p><p><a href="/wiki/Brazil_national_football_team" title="Brazil national football team">Brazil</a> announced their final squad on 7 November 2022.<sup id="cite_ref-59" class="reference"><a href="#cite_note-59">[58]</a></sup>
                </p>
                <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r886046722">
                <table class="sortable wikitable plainrowheaders jquery-tablesorter" style="font-size:100%; width: 98%">


                <thead>
                    <tr>
                        <th scope="col" style="width:5%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><abbr title="Number">No.</abbr>
                        </th>
                        <th scope="col" style="width:5%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><abbr title="Position">Pos.</abbr>
                        </th>
                        <th scope="col" style="width:30%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Player
                        </th>
                        <th scope="col" style="width:20%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Date of birth (age)
                        </th>
                        <th scope="col" style="width:5%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Caps
                        </th>
                        <th scope="col" style="width:5%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Goals
                        </th>
                        <th scope="col" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Club
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="nat-fs-player">
                        <td>1</td>
                        <td><span style="display:none">1</span><a href="/wiki/Goalkeeper_(association_football)" title="Goalkeeper (association football)">GK</a></td>
                        <th data-sort-value="Alisson" scope="row"><a href="/wiki/Alisson" class="mw-redirect" title="Alisson">Alisson</a></th>
                        <td style="text-align:left"><span style="display:none"> (<span class="bday">1992-10-02</span>)</span>2 October 1992 (aged 30)</td>
                        <td>57</td>
                        <td>0</td>
                        <td style="text-align:left"><span class="flagicon"><a href="/wiki/The_Football_Association" title="The Football Association"><img alt="England" src="//upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/23px-Flag_of_England.svg.png" decoding="async" width="23" height="14" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/35px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/46px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480"></a></span> <a href="/wiki/Liverpool_F.C." title="Liverpool F.C.">Liverpool</a></td>
                    </tr>
                    <tr class="nat-fs-player">
                        <td>2</td>
                        <td><span style="display:none">2</span><a href="/wiki/Defender_(association_football)" title="Defender (association football)">DF</a></td>
                        <th data-sort-value="Danilo" scope="row"><a href="/wiki/Danilo_(footballer,_born_July_1991)" title="Danilo (footballer, born July 1991)">Danilo</a></th>
                        <td style="text-align:left"><span style="display:none"> (<span class="bday">1991-07-15</span>)</span>15 July 1991 (aged 31)</td>
                        <td>46</td>
                        <td>1</td>
                        <td style="text-align:left"><span class="flagicon"><a href="/wiki/Italian_Football_Federation" title="Italian Football Federation"><img alt="Italy" src="//upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/23px-Flag_of_Italy.svg.png" decoding="async" width="23" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/35px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/45px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000"></a></span> <a href="/wiki/Juventus_F.C." class="mw-redirect" title="Juventus F.C.">Juventus</a></td>
                     </tr>

            </html>
        """

        mock_get.return_value = mock_response

        year = 2026
        fifa = Fifa(year)

        self.assertIsInstance(fifa.data, dict)
        self.assertIn('Brazil', fifa.data)
        assert (fifa.data['Brazil'][0]['player_name'], 'Alisson')
        assert (fifa.data['Brazil'][0]['dob'], '1992-10-02')
        assert (fifa.get_duplicate_bday_count(), 0)


if __name__ == '__main__':
    unittest.main()
