<h1>Battle Furry Heroes</h1>

<table>
    <tr>
        <td>
            <b>Objetivo:</b>
            <p>O projeto Battle Furry Heroes apresenta um desafio intrigante: desenvolver a lógica de um jogo de vídeo game que simula batalhas entre heróis mágicos. Ambientado no encantador Glimmer Glen, um local repleto de animais com poderes únicos e mágicos, o objetivo é criar uma experiência de batalha envolvente e divertida, levando em consideração as regras e mecânicas específicas definidas para o jogo.</p>
        </td>
    </tr>
</table>

<h2>Heróis</h2>
<table style="border-collapse: collapse; width: 800px; margin: 0 auto;">
    <tr>
        <td style="border: 1px solid black; text-align: center;">
            <p>Puppie</p>
            <img src="./docs/Puppie.gif" alt="Battle Furry Heroes" width="60" height="60">
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Força: 3000</p>
            <p>Defesa: 3000</p>
            <p>Velocidade: 4000</p>
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Twinkee</p>
            <img src="./docs/Twinkee.gif" alt="Battle Furry Heroes" width="60" height="60">
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Força: 4000</p>
            <p>Defesa: 3000</p>
            <p>Velocidade: 3000</p>
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Allepy</p>
            <img src="./docs/Allepy.gif" alt="Battle Furry Heroes" width="60" height="60">
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Força: 3000</p>
            <p>Defesa: 4000</p>
            <p>Velocidade: 3000</p>
        </td>
    </tr>
    <tr>
        <td style="border: 1px solid black; text-align: center;">
            <p>Whispy</p>
            <img src="./docs/Whispy.gif" alt="Battle Furry Heroes" width="60" height="60">
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Força: 3500</p>
            <p>Defesa: 3500</p>
            <p>Velocidade: 3000</p>
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Mimzy</p>
            <img src="./docs/Mimzy.gif" alt="Battle Furry Heroes" width="60" height="60">
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Força: 3000</p>
            <p>Defesa: 3500</p>
            <p>Velocidade: 3500</p>
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Blinky</p>
            <img src="./docs/Blinky.gif" alt="Battle Furry Heroes" width="60" height="60">
        </td>
        <td style="border: 1px solid black; text-align: center;">
            <p>Força: 3200</p>
            <p>Defesa: 3200</p>
            <p>Velocidade: 3600</p>
        </td>
    </tr>
</table>

<h2>Totens</h2>
<table style="border-collapse: collapse; width: 800px; margin: 0 auto;">
    <tr>
        <th style="border: 1px solid black;">Categoria</th>
        <th style="border: 1px solid black;">Totens</th>
        <th style="border: 1px solid black;">Bônus</th>
    </tr>
    <tr>
        <td style="border: 1px solid black;">Força</td>
        <td style="border: 1px solid black;">
            <ul>
                <li>Luvas do Titã</li>
                <li>Cristal de Fúria</li>
                <li>Porção de Força</li>
                <li>Pedra do Poder</li>
                <li>Machado Berserker</li>
                <li>Lâmina da Destruição</li>
                <li>Anel do Golpe Devastador</li>
                <li>Totem do Guerreiro Ancestral</li>
            </ul>
        </td>
        <td style="border: 1px solid black;">500 - 1500</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">Defesa</td>
        <td style="border: 1px solid black;">
            <ul>
                <li>Aura de Armadura</li>
                <li>Escudo Divino</li>
                <li>Cota de Malha Mística</li>
                <li>Barreira Elemental</li>
                <li>Elmo do Guardião</li>
                <li>Amuleto da Proteção Absoluta</li>
                <li>Essência do Rochedo</li>
                <li>Runas do Guardião</li>
            </ul>
        </td>
        <td style="border: 1px solid black;">500 - 1500</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">Velocidade</td>
        <td style="border: 1px solid black;">
            <ul>
                <li>Elixir da Velocidade</li>
                <li>Botas Aladas</li>
                <li>Manto do Vento</li>
                <li>Adaga da Agilidade</li>
                <li>Braceletes da Celeridade</li>
                <li>Capa das Sombras Rápidas</li>
                <li>Cristal do Teleporte Rápido</li>
                <li>Talismã do Corredor Fantasma</li>
            </ul>
        </td>
        <td style="border: 1px solid black;">500 - 1500</td>
    </tr>
</table>

<h3>🕹️ Regras & mecânicas:</h3>

<b>Objetivo:</b>

<p>O objetivo do jogo é que os heróis batalhem entre si utilizando seus atributos de Força, Defesa e Velocidade, além de bônus proporcionados pelos totens escolhidos. O jogo se desenrola em diversas batalhas até que reste apenas um herói vencedor.</p>

<b>Jogadores:</b>

<ul>
  <li>O Computador deve receber dois personagens para disputar a batalha, juntamente com o totem desejado.</li>
</ul>

<b>Batalhas:</b>

<ul>
  <li>Os heróis irão batalhar entre si em rodadas sucessivas até que reste apenas um.</li>
  <li>A cada batalha, será escolhido um novo totem adicional para aumentar o poder do herói.</li>
  <li>As batalhas continuam até que um único herói permaneça como vencedor final.</li>
</ul>

<b>Classificação de Nível:</b>

<ul>
  <li>O poder total do herói é determinado pela soma de seus atributos (Força, Defesa, Velocidade) e o bônus do totem.</li>
  <li>Os níveis dos heróis são classificados conforme a tabela abaixo:</li>
</ul>

<table style="border-collapse: collapse; width: 400px; margin: 0 auto;">
    <tr>
        <th style="border: 1px solid black;">Poder Total</th>
        <th style="border: 1px solid black;">Nível</th>
    </tr>
    <tr>
        <td style="border: 1px solid black;">&lt; 1000</td>
        <td style="border: 1px solid black;">Ferro</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">1001 - 2000</td>
        <td style="border: 1px solid black;">Bronze</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">2001 - 5000</td>
        <td style="border: 1px solid black;">Prata</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">5001 - 7000</td>
        <td style="border: 1px solid black;">Ouro</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">7001 - 8000</td>
        <td style="border: 1px solid black;">Platina</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">8001 - 9000</td>
        <td style="border: 1px solid black;">Ascendente</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">9001 - 10000</td>
        <td style="border: 1px solid black;">Imortal</td>
    </tr>
    <tr>
        <td style="border: 1px solid black;">&gt; 10000</td>
        <td style="border: 1px solid black;">Radiante</td>
    </tr>
</table>
