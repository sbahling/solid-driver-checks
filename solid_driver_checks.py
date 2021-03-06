import parameters
from utils import input_data
from utils import export
from utils import remote_check
from utils import checks
import os

if __name__ == "__main__":
    args = parameters.parameter_parse()

    if args.dir != None:
        rpmCheck = checks.RPMChecks()
        check_result = rpmCheck.AnalysisDir(path=args.dir, query=args.query)

        if args.output == 'terminal':
            export.rpms_export_to_terminal(check_result)
        elif args.output == 'html':
            export.rpms_export_to_html(check_result, args.file)
        elif args.output == 'pdf':
            export.rpms_export_to_pdf(check_result, args.file)
        elif args.output == 'excel':
            export.rpms_export_to_excel(check_result, args.file)
    elif args.rpm != None:
        rpmCheck = checks.RPMChecks()
        check_result = rpmCheck.analysisRPM(args.rpm)
        print(check_result)
    elif args.system:
        driverCheck = checks.DriverChecks()
        check_result = driverCheck.AnalysisOS(args.query)

        if args.output == 'terminal':
            export.os_export_to_terminal(check_result)
        elif args.output == 'html':
            export.os_export_to_html(check_result, args.file)
        elif args.output == 'pdf':
            export.os_export_to_pdf(check_result, args.file)
        elif args.output == 'excel':
            result = dict()
            result['Solid Driver Checks'] = check_result
            export.os_export_to_excel(result, args.file)
    elif args.driver != None:
        driverCheck = checks.DriverChecks()
        driver_support_flag, running, rpm_info = driverCheck.Analysis(args.driver)
        export.print_driver(args.driver, driver_support_flag, running, rpm_info)
    elif args.remote != None:
        servers = remote_check.get_remote_server_config(args.remote)
        check_result = remote_check.check_remote_servers(servers)

        if args.output == 'terminal':
            export.remote_export_to_terminal(check_result)
        elif args.output == 'html':
            export.remote_export_to_html(check_result, args.file)
        elif args.output == 'pdf':
            export.remote_export_to_pdf(check_result, args.file)
        elif args.output == 'excel':
            if os.path.exists(args.file):
                os.remove(args.file)
            export.remote_export_to_excel(check_result, args.file)


