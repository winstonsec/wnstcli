import click
from wnstcli.modules.install import install
from wnstcli.modules.hardening import hardening

from colorama import init, Fore, Style

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        ascii_art = (
            f"{Fore.WHITE}"
            "                                                                                                    \n"
            "                                                                           &&&&&                    \n"
            "                                                                       #&&&&&&&&&&&&                \n"
            "                                                                 *&&&&&&&&&&%  &&&&&&&&&&&          \n"
            "                                                        &&&&&&&&&&&&&&&&           &&&&&&&&&&&&&&&&&\n"
            "                                                        &&&&&&&&&&                        &&&&&&&&&&\n"
            "                                                        &&&&&                                  &&&&&\n"
            "   &&&&&&&&      &&&&      &&&&&&&&/  &&&&&&&&&         &&&&&          ///     ////////        &&&&&\n"
            "  &&            && &&&     &&&        &&&                &&&&       ///   ///  ///   //        &&&& \n"
            "  &&&&&&&&     &&&  &&&    &&&&&&&&   &&&&&&&&           &&&&&      //   ////  ///////        &&&&& \n"
            "        &&&   &&&&&&&&&    &&&        &&&                 &&&&&     ///    //  ///   ///      &&&&& \n"
            " &&&&&&&&&&  &&&     &&&   &&&        &&&&&&&&&           &&&&&&      ///////  ////////        &&&  \n"
            "                                                           &&&&&&                                   \n"
            "                                                             &&&&&                                  \n"
            "                                                              &&&&&&                    /////       \n"
            f"{Fore.MAGENTA}"
            "                                                                                      //////        \n"
            "                                                                                   ///////          \n"
            "                                                                      /////      //////             \n"
            "                                                                       //////.///////               \n"
            "                                                                         /////////                  \n"
            "                                                                            ////                    \n"
            f"{Style.RESET_ALL}"
            "// Tá seguro? tá beleza!                                                                            \n"
            "                                                                                                    \n"
        )
        click.echo(ascii_art)
        click.echo(" ")
        click.echo(ctx.get_help())

cli.add_command(install.install)
cli.add_command(hardening.hardening)


if __name__ == '__main__':
    cli()
