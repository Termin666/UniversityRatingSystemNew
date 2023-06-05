import * as React from "react";
import { Box } from "@mui/material"
import { Navigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import ReportListContainer from "../components/ReportListContainer";
import CreateReportDialog from "../components/CreateReportDialog";
import styles from "../styles/Page.module.css";


export default function ReportsPage({ logout, isAuthenticated }) {
    const [isOpen, setOpenCreateReport] = React.useState(false);

    const handleClickOpenCreateReport = () => {
        setOpenCreateReport(true);
    };

    const handleCloseCreateReport = () => {
        setOpenCreateReport(false);
    };

    const onCreateReport = () => {
        // TODO send request to api
    };

    const navbarActions = [
        {name: "Создать анкету", func: handleClickOpenCreateReport},
        {name: "Выйти", func: logout}
    ]

    var reports = [{id: 1}, {id: 2}, {id: 3}]

    const availableEducators = [{label: "Фамилия Имя Отчество", value: "TestName"}]
    const availableYears = [{label: "2023", value: "2023"}]

    if (false) {    // TODO: not isAuthenticated
        return <Navigate to='/login' />
    }


    return (
        <>
            <Navbar actions={ navbarActions } pageTitle={ "Фамилия Имя Отчество" } />
            <Box className={ `${styles.center} ${styles.pageTopStart}` }>
                <ReportListContainer reports={ reports }/>
            </Box>
            <CreateReportDialog 
                isOpen={ isOpen }
                onClose={ handleCloseCreateReport }
                onCreate={ onCreateReport } 
                availableYears={ availableYears }
                availableEducators={ availableEducators }
            />
        </>
    );
}
